"""Per-record JSON-LD documents and their safe embedding (site spec §2.3)."""
import json

import rdflib
from rdflib import RDF, URIRef

from solar_kb.export import jsonld_context
from solar_kb.iri import KB, load_prefixes
from solar_kb.records import load_corpus
from solar_kb.site.jsonld import CONTEXT_URL, record_document, script_json
from tests.helpers import FIXTURES, SCHEMA


def test_record_document_parses_to_the_record_iri():
    record = load_corpus(FIXTURES / "mini").records["fm:pid"]
    doc = record_document(record, load_prefixes(SCHEMA), context=jsonld_context(SCHEMA))
    g = rdflib.Graph().parse(data=json.dumps(doc), format="json-ld")
    assert (URIRef(KB + "fm/pid"), RDF.type, URIRef(KB + "FailureMode")) in g
    assert URIRef(KB + "mit/pid-recovery") in set(g.objects(None, URIRef(KB + "target")))


def test_record_document_references_the_published_context():
    record = load_corpus(FIXTURES / "mini").records["fm:pid"]
    assert record_document(record, load_prefixes(SCHEMA))["@context"] == CONTEXT_URL == KB + "solar_kb.context.jsonld"


def test_script_json_cannot_close_the_script_tag():
    out = script_json({"body": "</script><script>alert(1)</script>"})
    assert "</script" not in out and json.loads(out)["body"] == "</script><script>alert(1)</script>"
