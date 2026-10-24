"""Schema 0.5.0 validator rules (spec B §4.3-4.4, §6 item 6, decision 2): relation pairs, scope, negated,
quote_source and the quote cap, identity slots, FaultCode firmware scope, and the related_to lint."""
import pytest
from typer.testing import CliRunner

from solar_kb.cli import app
from solar_kb.records import load_corpus
from solar_kb.rules import ALL_RULES, lint_corpus
from tests.helpers import REPO, copy_fixture, copy_schema, write_record

H = "a1b2c3d4e5f6"
MANUAL = f'[{{src: "src:b0-vendor-manual", loc: "sec=1", h: "{H}"}}]'
CODE = f'[{{src: "src:b0-electrical-code", loc: "sec=1", h: "{H}"}}]'


def hits(root):
    corpus = load_corpus(root)
    return {(v.rule, v.record_id, v.claim_id) for rule in ALL_RULES for v in rule(corpus)}


def messages(root, rule):
    corpus = load_corpus(root)
    return [v.message for r in ALL_RULES for v in r(corpus) if v.rule == rule]


def probe(root, type_dir, prefix, rtype, front="", claims="", slug="probe"):
    write_record(root, type_dir, slug, f"id: {prefix}:{slug}\ntype: {rtype}\nname: Probe\n{front}"
                 + (f"claims:\n{claims}" if claims else ""))
    return f"{prefix}:{slug}"


def claim(rel, target, extra="", cite=MANUAL, review="drafted", n=1):
    return f"  - claim_id: c{n}\n    rel: {rel}\n    target: {target}\n{extra}    cite: {cite}\n    review: {review}\n"


@pytest.fixture
def root(tmp_path):
    return copy_fixture(tmp_path, "b0")


def test_b0_fixture_passes_every_rule(root):
    assert hits(root) == set()


def test_real_records_pass_every_rule():
    corpus = load_corpus(REPO)
    assert [str(v) for rule in ALL_RULES for v in rule(corpus)] == []


# --- relation pairs ---------------------------------------------------------------------------------------------

@pytest.mark.parametrize("type_dir, prefix, rtype, rel, target, ok", [
    ("products", "prod", "Product", "instance_of", "comp:string-inverter", True),
    ("products", "prod", "Product", "instance_of", "std:nec-2023", False),  # a GridProfile's pair, not a Product's
    ("grid-profiles", "profile", "GridProfile", "instance_of", "std:nec-2023", True),
    ("parameters", "param", "Parameter", "instance_of", "param:ov2-trip-voltage", True),
    ("parameters", "param", "Parameter", "instance_of", "comp:string-inverter", False),
    ("concepts", "concept", "Concept", "subclass_of", "concept:maximum-power-point", True),
    ("concepts", "concept", "Concept", "subclass_of", "func:rapid-shutdown", False),  # subclass_of stays in a type
    ("standards", "std", "Standard", "supersedes", "std:nec-2023", True),
    ("standards", "std", "Standard", "supersedes", "prod:sma-stp-core1-us", False),
    ("hazards", "hazard", "Hazard", "part_of", "proc:commission-stp-core1", True),  # part_of is * -> *
    ("firmware-releases", "fw", "FirmwareRelease", "fixes", "func:rapid-shutdown", True),
    ("firmware-releases", "fw", "FirmwareRelease", "fixes", "tool:insulation-tester", False),
    ("tools", "tool", "Tool", "implements", "func:rapid-shutdown", False),  # implements is Product/FirmwareRelease only
])
def test_relation_pairs(root, type_dir, prefix, rtype, rel, target, ok):
    front = {"Product": "make: sma\nproduct_level: family\n", "GridProfile": "make: sma\nprofile_code: X\n",
             "Concept": "concept_kind: physics\n", "Standard": "standard_kind: code\n",
             "FirmwareRelease": "product: prod:sma-stp-core1-us\nversion: '1.0'\n",
             "Tool": "tool_kind: instrument\n"}.get(rtype, "")
    rid = probe(root, type_dir, prefix, rtype, front, claim(rel, target))
    assert (("targets", rid, "c1") in hits(root)) is not ok


def test_caused_by_accepts_the_widened_range(root):
    probe(root, "failure-modes", "fm", "FailureMode", claims=claim("caused_by", "param:sma-reconnect-voltage-max")
          + claim("caused_by", "arch:ac-coupled-storage", n=2) + claim("caused_by", "func:rapid-shutdown", n=3))
    assert {(r, c) for r, rid, c in hits(root) if rid == "fm:probe"} == {("targets", "c3")}


# --- scope ------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("scope, ok", [
    ("products: [prod:sma-stp-62-us-41]\n      regions: [region:us-ca]\n      standard: std:nec-2023", True),
    ("architecture: arch:ac-coupled-storage\n      applications: [backup, off-grid]", True),
    ("firmware_min: '2.0'\n      firmware_max: '3.1'", True),
    ("products: [prod:nope]", False),  # missing id
    ("regions: [prod:sma-stp-62-us-41]", False),  # wrong type
    ("standard: req:nec-2023-690-12-b-2", False),  # a Requirement is not a Standard edition
    ("firmware_min: '3.12'\n      firmware_max: '3.2'", False),  # 3.12 is after 3.2
    ("valid_from: 2026-01-02\n      valid_to: 2026-01-01", False),
])
def test_scope(root, scope, ok):
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n",
          claim("compatible_with", "arch:ac-coupled-storage", f"    scope:\n      {scope}\n"))
    assert (("scope", "prod:probe", "c1") in hits(root)) is not ok


def test_empty_scope_is_reported(root):
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n",
          claim("compatible_with", "arch:ac-coupled-storage", "    scope: {}\n"))
    assert ("scope", "prod:probe", "c1") in hits(root)


def test_public_scope_cannot_name_a_private_record(root, tmp_path):
    overlay = tmp_path / "overlay"
    write_record(overlay, "products", "secret", "id: prod:secret\ntype: Product\nname: Secret\nstatus: proposed")
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n",
          claim("compatible_with", "arch:ac-coupled-storage", "    scope:\n      products: [prod:secret]\n"))
    corpus = load_corpus(root, overlay)
    assert any(v.rule == "layers" and v.record_id == "prod:probe" for rule in ALL_RULES for v in rule(corpus))


# --- negated ----------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("rel, target, value, ok", [
    ("compatible_with", "arch:ac-coupled-storage", "true", True),
    ("certified_to", "std:nec-2023", "true", True),
    ("implements", "func:rapid-shutdown", "true", False),  # use lacks
    ("lacks", "func:rapid-shutdown", "true", False),  # no double negatives
    ("part_of", "prod:sma-stp-core1-us", "true", False),
    ("compatible_with", "arch:ac-coupled-storage", "false", False),  # write it only as true
])
def test_negated(root, rel, target, value, ok):
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n",
          claim(rel, target, f"    negated: {value}\n"))
    assert (("negated", "prod:probe", "c1") in hits(root)) is not ok


def test_negated_on_a_quantity_is_reported(root):
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n",
          "  - claim_id: c1\n    attr: max_units\n    value: {max: 50, unit: unit:NUM}\n    conditions: x\n"
          f"    negated: true\n    cite: {MANUAL}\n    review: drafted\n")
    assert ("negated", "prod:probe", "c1") in hits(root)


def test_assert_and_negate_need_different_scopes(root):
    both = claim("compatible_with", "arch:ac-coupled-storage") + \
        claim("compatible_with", "arch:ac-coupled-storage", "    negated: true\n", n=2)
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n", both)
    assert ("negated", "prod:probe", "c2") in hits(root)
    scoped = claim("compatible_with", "arch:ac-coupled-storage") + claim(
        "compatible_with", "arch:ac-coupled-storage", "    negated: true\n    scope:\n      applications: [backup]\n", n=2)
    probe(root, "products", "prod", "Product", "make: sma\nproduct_level: family\n", scoped)
    assert not {h for h in hits(root) if h[1] == "prod:probe"}


# --- quote_source and the quote cap -----------------------------------------------------------------------------

LONG = " ".join(["placeholder"] * 40)


@pytest.mark.parametrize("type_dir, prefix, rtype, front, extra, cite, rule", [
    # a Requirement quoting a code in full, attributed: allowed (the fixture's req: record does exactly this)
    ("requirements", "req", "Requirement", "clause: '1.1'\n", f"    quote: {LONG}\n    quote_source: X 2023 §1.1\n",
     CODE, None),
    # the cap stays without attribution, or when the source is not a code or standard
    ("requirements", "req", "Requirement", "clause: '1.1'\n", f"    quote: {LONG}\n", CODE, "claim-shape"),
    ("requirements", "req", "Requirement", "clause: '1.1'\n", f"    quote: {LONG}\n    quote_source: X 2023 §1.1\n",
     MANUAL, "quote-source,claim-shape"),  # not a code source: no attribution, and the cap stays
    # outside Requirement records a code quote is attributed but still capped at 25 words
    ("functions", "func", "Function", "function_kind: protection\n",
     f"    quote: {LONG}\n    quote_source: X 2023 §1.1\n", CODE, "claim-shape"),
    ("functions", "func", "Function", "function_kind: protection\n",
     "    quote: short words only\n    quote_source: X 2023 §1.1\n", CODE, None),
    # quote_source needs a quote, and is never blank
    ("functions", "func", "Function", "function_kind: protection\n", "    quote_source: X 2023 §1.1\n", CODE,
     "quote-source"),
    ("functions", "func", "Function", "function_kind: protection\n", "    quote: a b\n    quote_source: ' '\n", CODE,
     "quote-source"),
])
def test_quote_source_and_cap(root, type_dir, prefix, rtype, front, extra, cite, rule):
    claims = claim("requires", "func:rapid-shutdown" if rtype == "Requirement" else "role:installer", extra, cite=cite)
    if rtype == "Requirement":
        claims += claim("part_of", "std:nec-2023", cite=CODE, n=2)
    rid = probe(root, type_dir, prefix, rtype, front, claims)
    got = {r for r, i, c in hits(root) if i == rid and c == "c1"}
    assert got == (set(rule.split(",")) if rule else set())


# --- identity slots ---------------------------------------------------------------------------------------------

@pytest.mark.parametrize("type_dir, prefix, rtype, front, claims, ok", [
    ("products", "prod", "Product", "make: sma\nproduct_level: family\n", "", True),
    ("products", "prod", "Product", "product_level: family\n", "", False),  # make missing
    ("products", "prod", "Product", "status: proposed\n", "", True),  # stubs carry no identity
    ("products", "prod", "Product", "make: acme\nproduct_level: family\n", "", False),  # no org:acme
    ("products", "prod", "Product", "make: sma\nproduct_level: model\nmodel_number: M1\n",
     claim("part_of", "prod:sma-stp-core1-us"), True),
    ("products", "prod", "Product", "make: sma\nproduct_level: model\n", claim("part_of", "prod:sma-stp-core1-us"),
     False),  # model_number missing
    ("products", "prod", "Product", "make: sma\nproduct_level: model\nmodel_number: M1\n", "", False),  # no family
    ("requirements", "req", "Requirement", "clause: '1'\n", claim("part_of", "std:nec-2023", cite=CODE), True),
    ("requirements", "req", "Requirement", "clause: '1'\n", "", False),  # not part_of a Standard
    ("firmware-releases", "fw", "FirmwareRelease", "product: prod:sma-stp-core1-us\nversion: '1'\n", "", True),
    ("firmware-releases", "fw", "FirmwareRelease", "product: org:sma\nversion: '1'\n", "", False),  # not a Product
    ("parameters", "param", "Parameter", "access_level: tool:insulation-tester\n", "", False),  # not a Role
    ("standards", "std", "Standard", "standard_kind: grid-code\njurisdiction: region:nowhere\n", "", False),
    ("organizations", "org", "Organization", "", "", False),  # org_kind missing
    ("registers", "reg", "Register", "make: sma\naddress: '0x1F40'\n", "", True),
])
def test_identity(root, type_dir, prefix, rtype, front, claims, ok):
    rid = probe(root, type_dir, prefix, rtype, front, claims)
    assert (any(r == "identity" and i == rid for r, i, _ in hits(root))) is not ok


# --- FaultCode firmware scope -----------------------------------------------------------------------------------

FC = """id: {id}
type: FaultCode
name: SMA STP CORE1 3501
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US
code: "3501"
code_key: "3501"
category: Inverters
{fw}claims:
  - claim_id: c1
    rel: defined_in
    target: src:b0-vendor-manual
    cite: [{{src: "src:b0-vendor-manual", loc: "tbl=1.r2", h: "a1b2c3d4e5f6"}}]
    review: drafted
"""


@pytest.mark.parametrize("slug, fw, ok", [
    ("sma-stp-core1-us-3501", "", True),  # no firmware scope: the 0.4.0 id
    ("sma-stp-core1-us-3501-fw-4-0", "firmware_min: '4.0'\n", True),
    ("sma-stp-core1-us-3501-fw-upto-2-1", "firmware_max: '2.1'\n", True),
    ("sma-stp-core1-us-3501", "firmware_min: '4.0'\n", False),  # a firmware-scoped code needs the suffix
    ("sma-stp-core1-us-3501-fw-4-0", "firmware_min: '4.0'\nfirmware_max: '3.9'\n", False),  # out of order
])
def test_fault_code_firmware_scope(root, slug, fw, ok):
    write_record(root, "fault-codes", slug, FC.format(id=f"fc:{slug}", fw=fw))
    assert (any(r == "fault-code" and i == f"fc:{slug}" for r, i, _ in hits(root))) is not ok


def test_new_rules_survive_garbage_shapes(root):
    write_record(root, "products", "garbage",
                 "id: prod:garbage\ntype: Product\nname: G\nmake: [sma]\nproduct_level: {a: 1}\nproduct: [x]\n"
                 "claims:\n  - claim_id: c1\n    rel: [related_to]\n    target: {x: 1}\n    negated: [true]\n"
                 "    scope: [products]\n    quote_source: 5\n    cite: nope\n"
                 "  - claim_id: c2\n    rel: compatible_with\n    negated: true\n    scope: {products: {a: 1}, regions: 5,"
                 " firmware_min: [1], valid_from: [2]}\n    quote_source: [x]\n    cite: [nope, {src: [1]}]\n"
                 "  - claim_id: c3\n    rel: [x]\n    negated: true\n    target: [y]\n")
    write_record(root, "fault-codes", "garbage", "id: fc:garbage\ntype: FaultCode\nname: G\nfirmware_min: {a: 1}\n"
                 "firmware_max: [2]")
    corpus = load_corpus(root)
    for rule in ALL_RULES:
        rule(corpus)  # must not raise
    lint_corpus(corpus)


# --- related_to lint --------------------------------------------------------------------------------------------

def test_related_to_is_a_warning_naming_the_typed_alternatives(root):
    probe(root, "concepts", "concept", "Concept", "concept_kind: physics\n",
          claim("related_to", "concept:maximum-power-point"))
    assert hits(root) == set()  # never a violation
    [warning] = [w for w in lint_corpus(load_corpus(root)) if w.record_id == "concept:probe"]
    assert warning.rule == "lint-related-to" and "explains" in warning.message and "subclass_of" in warning.message


def test_cli_validate_prints_warnings_and_passes(root):
    copy_schema(root)
    probe(root, "concepts", "concept", "Concept", "concept_kind: physics\n",
          claim("related_to", "metric:performance-ratio"))
    result = CliRunner().invoke(app, ["validate", "--root", str(root)])
    assert result.exit_code == 0, result.output
    assert "warning: [lint-related-to] concept:probe#c1" in result.output and "1 warning(s)" in result.output
