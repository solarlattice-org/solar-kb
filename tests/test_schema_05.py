"""Schema 0.5.0 (spec B §4): modules, the 21 new types, relations, claim extensions; every IRI of 0.4.0 kept."""
from pathlib import Path

import pytest
import rdflib
import yaml
from linkml_runtime.utils.schemaview import SchemaView

from solar_kb.export import export_all
from solar_kb.iri import KB, load_prefixes
from solar_kb.records import TYPE_DIRS, Record, load_corpus
from solar_kb.rules import ALL_RULES, RELATION_PAIRS, RELATION_SIGNATURES
from solar_kb.schema_check import SchemaChecker
from tests.helpers import FIXTURES, REPO, SCHEMA

MODULES = ("core", "failure", "equipment", "events", "control", "communication", "practice", "regulation",
           "engineering", "overlay")
NEW_TYPES = {  # type -> (prefix, module) per spec B §4.1
    "Organization": ("org", "core"), "Region": ("region", "core"), "Role": ("role", "core"),
    "Product": ("prod", "equipment"), "FirmwareRelease": ("fw", "equipment"), "Tool": ("tool", "equipment"),
    "OperatingState": ("state", "events"), "Function": ("func", "control"), "Parameter": ("param", "control"),
    "GridProfile": ("profile", "control"), "Protocol": ("proto", "communication"), "Register": ("reg", "communication"),
    "Procedure": ("proc", "practice"), "Hazard": ("hazard", "practice"), "Standard": ("std", "regulation"),
    "Requirement": ("req", "regulation"), "Program": ("prog", "regulation"), "Concept": ("concept", "engineering"),
    "Metric": ("metric", "engineering"), "CalculationMethod": ("calc", "engineering"),
    "Architecture": ("arch", "engineering"),
}
# Every class, slot and enum of schema 0.4.0 (they keep their kb: IRIs)
OLD_CLASSES = {"Record", "FailureMode", "Stressor", "Symptom", "Measurement", "DetectionMethod", "Mitigation",
               "Component", "Source", "FaultCode", "EventConcept", "Case", "DataExample", "Claim", "Citation",
               "QuantityValue", "Signal"}
OLD_ENUMS = {"RecordStatus", "Relation", "EventAxis", "ReviewState", "KeepState", "SourceTier", "TdmOk"}
NEW_RELATIONS = {"subclass_of", "part_of", "instance_of", "manufactured_by", "issued_by", "adopted_in", "supersedes",
                 "applies_to", "implements", "lacks", "requires", "configures", "sets_value_of", "compatible_with",
                 "incompatible_with", "certified_to", "fixes", "introduces", "uses_protocol", "exposes", "maps_to",
                 "indicates_state", "performed_by", "uses_tool", "has_hazard", "controlled_by", "defines", "explains",
                 "related_to"}


@pytest.fixture(scope="module")
def view():
    return SchemaView(str(SCHEMA))


def test_root_imports_the_ten_modules_and_holds_every_prefix():
    root = yaml.safe_load(SCHEMA.read_text())
    assert root["version"] == "0.5.0"
    assert root["imports"] == ["linkml:types"] + [f"solar_kb_{m}" for m in MODULES]
    for m in MODULES:
        module = yaml.safe_load((REPO / "schema" / f"solar_kb_{m}.yaml").read_text())
        assert module["default_prefix"] == "kb" and module["prefixes"]["kb"] == KB
    prefixes = load_prefixes(SCHEMA)
    for prefix, _ in NEW_TYPES.values():
        assert prefixes[prefix] == f"{KB}{prefix}/" and prefix in root["prefixes"]


def test_each_new_type_lives_in_its_module_with_a_record_directory(view):
    by_type = {t: (d, p) for d, (t, p) in TYPE_DIRS.items()}
    for rtype, (prefix, module) in NEW_TYPES.items():
        cls = view.get_class(rtype)
        assert cls.is_a == "Record", rtype
        assert cls.from_schema.endswith(f"/schema/{module}"), (rtype, cls.from_schema)
        assert by_type[rtype][1] == prefix
        assert view.get_uri(rtype, expand=True) == KB + rtype


def test_old_terms_keep_their_iris(view):
    for name in OLD_CLASSES | OLD_ENUMS:
        assert view.get_uri(name, expand=True, native=False) == KB + name
    assert view.get_uri("src", expand=True, native=False) == KB + "cites_source"
    assert view.get_uri("close_mappings", expand=True, native=False) == "http://www.w3.org/2004/02/skos/core#closeMatch"


def test_owl_export_keeps_every_term_in_the_one_concept_scheme(tmp_path):
    export_all(load_corpus(FIXTURES / "mini"), SCHEMA, tmp_path)
    g = rdflib.Graph().parse(tmp_path / "solar_kb.owl.ttl", format="turtle")
    schemes = {str(o) for o in g.objects(predicate=rdflib.SKOS.inScheme)}
    assert schemes == {KB + "schema"}
    assert (rdflib.URIRef(KB + "Product"), rdflib.RDF.type, rdflib.OWL.Class) in g


def test_relation_enum_and_validator_table_agree(view):
    enum = set(view.get_enum("Relation").permissible_values)
    assert enum == set(RELATION_PAIRS) == set(RELATION_SIGNATURES)
    assert NEW_RELATIONS <= enum
    for value, pv in view.get_enum("Relation").permissible_values.items():
        assert pv.description and "->" in pv.description, value  # domain -> range documented


def test_caused_by_range_is_widened():
    _, targets = RELATION_SIGNATURES["caused_by"]
    assert targets == {"Stressor", "FailureMode", "Parameter", "GridProfile", "FirmwareRelease", "Architecture"}


def test_instance_of_pairs_are_exact():
    pairs = RELATION_PAIRS["instance_of"]
    assert pairs == {("Product", "Component"), ("Parameter", "Parameter"), ("GridProfile", "Standard")}
    assert ("Concept", "Concept") in RELATION_PAIRS["subclass_of"] and ("Concept", "Product") not in RELATION_PAIRS["subclass_of"]


def test_claim_extensions_and_enums(view):
    claim_slots = set(view.class_slots("Claim"))
    assert {"scope", "negated", "quote_source"} <= claim_slots
    assert set(view.class_slots("ClaimScope")) == {"products", "firmware_min", "firmware_max", "hardware_rev",
                                                    "regions", "applications", "architecture", "standard",
                                                    "valid_from", "valid_to"}
    assert {"firmware_min", "firmware_max"} <= set(view.class_slots("FaultCode"))
    assert "source_kind" in view.class_slots("Source")
    assert "certification-scheme" in view.get_enum("StandardKind").permissible_values
    for enum in ("OrgKind", "ProductLevel", "ToolKind", "FunctionKind", "ProtocolKind", "ProcedureKind", "StandardKind",
                 "ProgramKind", "ConceptKind", "RoleKind", "Application"):
        assert view.get_enum(enum).permissible_values, enum


def _record(data: dict, type_dir: str) -> Record:
    return Record(data=data, body="", path=Path("x.md"), layer="public", type_dir=type_dir)


def test_schema_rejects_bad_new_slot_values():
    checker = SchemaChecker(SCHEMA)
    bad = {"id": "prod:x", "type": "Product", "name": "X", "make": "sma", "product_level": "series",
           "claims": [{"claim_id": "c1", "rel": "part_of", "target": "prod:y", "negated": "yes",
                       "scope": {"applications": ["grid-tied"], "firmware_minimum": "1"},
                       "cite": [{"src": "src:a", "loc": "sec=1", "h": "a1b2c3d4e5f6"}], "review": "drafted"}]}
    messages = " | ".join(v.message for v in checker.check(_record(bad, "products")))
    assert "'series' is not one of" in messages and "'grid-tied' is not one of" in messages
    assert "'yes' is not of type 'boolean'" in messages
    bad["claims"][0].update(negated=True, scope={"firmware_minimum": "1"})  # scope is closed too
    messages = " | ".join(v.message for v in checker.check(_record(bad, "products")))
    assert "'firmware_minimum' was unexpected" in messages
    reg = {"id": "reg:x", "type": "Register", "name": "X", "address": "0xZZ", "access": "read"}
    messages = " | ".join(v.message for v in checker.check(_record(reg, "registers")))
    assert "does not match" in messages and "'read' is not one of" in messages


def test_one_fixture_record_of_each_new_type_validates():
    corpus = load_corpus(FIXTURES / "b0")
    assert {r.type for r in corpus.records.values()} >= set(NEW_TYPES)
    checker = SchemaChecker(SCHEMA)
    violations = [v for r in corpus.records.values() for v in checker.check(r)]
    violations += [v for rule in ALL_RULES for v in rule(corpus)]
    assert violations == []


def test_existing_fixtures_still_validate():
    corpus = load_corpus(FIXTURES / "mini", FIXTURES / "overlay")
    checker = SchemaChecker(SCHEMA)
    assert [v for r in corpus.records.values() for v in checker.check(r)] == []
