"""Site support for schema 0.5.0: every new type gets a type index, a term page and record pages (site spec §2, spec B
§7); record pages print identity slots, claim scope, negation and quote attribution, and list a record's parts."""
import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

from solar_kb.records import load_corpus
from solar_kb.site.build import build_site
from solar_kb.site.paths import record_path, term_path, type_index_path
from tests.helpers import FIXTURES, SCHEMA
from tests.test_schema_05 import NEW_TYPES


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    build_site(load_corpus(FIXTURES / "b0"), SCHEMA, out)  # raises on a dead link or a path collision
    return out


def test_every_new_type_has_index_term_and_record_pages(site):
    corpus = load_corpus(FIXTURES / "b0")
    for rtype, (prefix, _) in NEW_TYPES.items():
        assert (site / type_index_path(prefix)).is_file(), rtype
        assert (site / term_path("https://solarlattice.org/kb/" + rtype)).is_file(), rtype
        for record in (r for r in corpus.records.values() if r.type == rtype):
            page = (site / record_path(record.id)).read_text()
            assert record.data["name"] in page and f'href="../{rtype}"' in page, record.id
            assert (site / record_path(record.id).replace(".html", ".jsonld")).is_file()


def test_type_index_lists_records_and_term_page_describes_the_type(site):
    index = (site / "kb/prod/index.html").read_text()
    assert 'href="sma-stp-core1-us"' in index and "SMA STP 62-US-41" in index
    term = (site / "kb/Product.html").read_text()
    assert "family, model or variant" in term and "product_level" in term


def test_product_family_lists_its_models_and_identity(site):
    page = (site / "kb/prod/sma-stp-core1-us.html").read_text()
    assert "<h2>Models and variants</h2>" in page and 'href="sma-stp-62-us-41">SMA STP 62-US-41</a>' in page
    assert '<dt>Make</dt><dd><a href="../org/sma">sma</a></dd>' in page
    assert '<dt>Product level</dt><dd>family</dd>' in page


def test_standard_lists_its_requirements(site):
    page = (site / "kb/std/nec-2023.html").read_text()
    assert "<h2>Requirements</h2>" in page and 'href="../req/nec-2023-690-12-b-2"' in page
    assert '<dt>Jurisdiction</dt><dd><a href="../region/us">United States</a></dd>' in page


def test_claims_show_negation_scope_and_quote_attribution(site):
    page = (site / "kb/prod/sma-stp-core1-us.html").read_text()
    assert '<strong class="negated">not</strong>' in page
    assert '<span class="label">Scope:</span>' in page and "applications backup" in page
    assert '<a href="../region/us">United States</a>' in page and "firmware from 3.12.20.R" in page
    req = (site / "kb/req/nec-2023-690-12-b-2.html").read_text()
    assert "<footer>— NFPA 70 (NEC) 2023 §690.12(B)(2). Quoted with attribution" in req


def test_landing_lists_only_types_with_records_and_kb_home_lists_all(site):
    landing = (site / "index.html").read_text()
    assert "Products</span>" in landing and "Programs</span>" in landing
    kb = (site / "kb/index.html").read_text()
    assert all(f'href="{prefix}/"' in kb for prefix, _ in NEW_TYPES.values())


def test_landing_skips_empty_types(tmp_path):
    out = tmp_path / "site"
    build_site(load_corpus(FIXTURES / "mini"), SCHEMA, out)
    landing = (out / "index.html").read_text()
    assert "Failure modes</span>" in landing and "Products</span>" not in landing
    assert 'href="prod/"' in (out / "kb/index.html").read_text()


def test_schema_modules_are_published_beside_the_root(site):
    root = yaml.safe_load((site / "kb/solar_kb.yaml").read_text())
    for module in root["imports"][1:]:
        assert (site / "kb" / f"{module}.yaml").is_file(), module
    view = SchemaView(str(site / "kb/solar_kb.yaml"))  # the downloaded schema resolves its imports
    assert "Product" in view.all_classes()
