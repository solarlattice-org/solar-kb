import pytest

from solar_kb.records import load_corpus
from solar_kb.rules import ALL_RULES
from tests.helpers import FIXTURES, copy_fixture, write_record


def run_rules(corpus):
    out = []
    for rule in ALL_RULES:
        out += rule(corpus)
    return out


def hits(root, overlay=None):
    return {(v.rule, v.record_id, v.claim_id) for v in run_rules(load_corpus(root, overlay))}


def test_fixtures_pass_every_rule():
    assert run_rules(load_corpus(FIXTURES / "mini", FIXTURES / "overlay")) == []


def claim_record(root, claim: str, slug="probe", type_dir="failure-modes", rtype="FailureMode",
                 prefix="fm"):
    write_record(root, type_dir, slug,
                 f"id: {prefix}:{slug}\ntype: {rtype}\nname: Probe\nclaims:\n" + claim)


CITE = '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted\n'


@pytest.mark.parametrize("claim, rule", [
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:nope\n" + CITE, "targets"),
    ("  - claim_id: c1\n    rel: presents_as\n    target: comp:pv-module\n" + CITE, "targets"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:probe\n" + CITE, "targets"),
    ("  - claim_id: c1\n    rel: distinguished_from\n    target: fm:pid\n" + CITE, "distinguished-by"),
    ("  - claim_id: c1\n    rel: distinguished_from\n    target: fm:pid\n    by: mit:pid-recovery\n"
     + CITE, "distinguished-by"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n"
     '    cite: [{src: "src:nowhere", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: drafted\n', "sources-exist"),
    ("  - claim_id: c1\n    attr: typical_power_loss\n    value: {min: 5, unit: unit:PERCENT}\n"
     + CITE, "quantities"),
    ("  - claim_id: c1\n    attr: typical_power_loss\n    value: {min: 9, max: 2, unit: unit:PERCENT}\n"
     "    conditions: x\n" + CITE, "quantities"),
    ("  - claim_id: c1\n    attr: typical_power_loss\n    value: {unit: unit:PERCENT}\n"
     "    conditions: x\n" + CITE, "quantities"),
    ("  - claim_id: c1\n    rel: caused_by\n    attr: x\n    target: fm:pid\n" + CITE, "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n" + CITE, "claim-shape"),
    ("  - claim_id: c1\n    attr: typical_power_loss\n    conditions: x\n" + CITE, "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n    by: method:el-imaging\n" + CITE,
     "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n" + CITE
     + "  - claim_id: c1\n    rel: leads_to\n    target: fm:pid\n" + CITE, "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n    quote: "
     + " ".join(["word"] * 26) + "\n" + CITE, "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n    keep: drafted\n"
     '    cite: [{src: "src:iea-t13-failures", loc: "sec=1", h: "a1b2c3d4e5f6"}]\n    review: verified\n', "claim-shape"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n    conflicts_with: [\"fm:pid#c99\"]\n"
     + CITE, "claim-refs"),
    ("  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n    superseded_by: \"fm:gone#c1\"\n"
     + CITE, "claim-refs"),
])
def test_bad_claims_are_caught(tmp_path, claim, rule):
    root = copy_fixture(tmp_path, "mini")
    claim_record(root, claim)
    assert rule in {r for r, rid, _ in hits(root) if rid == "fm:probe"}


def test_relation_from_wrong_source_type(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    claim_record(root, "  - claim_id: c1\n    rel: presents_as\n    target: symptom:uniform-power-loss\n"
                 + CITE, slug="probe", type_dir="components", rtype="Component", prefix="comp")
    assert ("targets", "comp:probe", "c1") in hits(root)


@pytest.mark.parametrize("type_dir, front, expected", [
    ("failure-modes", "id: stressor:wrong-dir\ntype: Stressor\nname: X", "ids"),
    ("failure-modes", "id: fm:Bad_Slug\ntype: FailureMode\nname: X", "ids"),
    ("failure-modes", "id: fm:other-name\ntype: FailureMode\nname: X", "ids"),
])
def test_id_rules(tmp_path, type_dir, front, expected):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, type_dir, "wrong-dir" if "wrong-dir" in front else "Bad_Slug"
                 if "Bad_Slug" in front else "mismatch", front)
    assert expected in {r for r, _, _ in hits(root)}


def test_public_claim_citing_private_source(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    claim_record(root, "  - claim_id: c1\n    rel: caused_by\n    target: fm:pid\n"
                 '    cite: [{src: "src:omnidian-work-orders", loc: "p=1", h: "a1b2c3d4e5f6"}]\n    review: drafted\n')
    assert ("public-citations", "fm:probe", "c1") in hits(root, FIXTURES / "overlay")


def test_private_source_and_case_in_public_repo(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "sources", "secret", "id: src:secret\ntype: Source\nname: S\n"
                 "tier: private\ntdm_ok: unknown")
    write_record(root, "cases", "wo-1", "id: case:wo-1\ntype: Case\nname: WO\ndiagnosis: fm:pid")
    found = hits(root)
    assert ("layers", "src:secret", None) in found
    assert ("layers", "case:wo-1", None) in found


def test_public_record_linking_into_overlay(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    overlay = copy_fixture(tmp_path, "overlay")
    write_record(overlay, "failure-modes", "private-fm", "id: fm:private-fm\ntype: FailureMode\n"
                 "name: Private")
    claim_record(root, "  - claim_id: c1\n    rel: leads_to\n    target: fm:private-fm\n" + CITE)
    assert ("layers", "fm:probe", None) in hits(root, overlay)


def test_case_links(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    overlay = copy_fixture(tmp_path, "overlay")
    write_record(overlay, "cases", "wo-2", "id: case:wo-2\ntype: Case\nname: WO 2\n"
                 "observed: [fm:pid]\ndiagnosis: symptom:uniform-power-loss")
    found = {r for r, rid, _ in hits(root, overlay) if rid == "case:wo-2"}
    assert found == {"case-links"}


def test_rules_survive_garbage_shapes(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "garbage",
                 "id: fm:garbage\ntype: FailureMode\nname: G\nclaims:\n  - just a string\n"
                 "  - claim_id: 7\n    rel: [a]\n    target: {x: 1}\n    cite: nope\n"
                 "    value: 12\n    conflicts_with: [3]\n"
                 "  - claim_id: c2\n    rel: caused_by\n    conflicts_with: 3\n    superseded_by: [x]\n"
                 "    quote: 5\n    cite: [nope, {src: [1]}]\n")
    overlay = copy_fixture(tmp_path, "overlay")
    write_record(overlay, "cases", "garbage", "id: case:garbage\ntype: Case\nname: G\n"
                 "observed: 5\ndiagnosis: [fm:pid]")
    run_rules(load_corpus(root, overlay))  # must not raise


@pytest.mark.parametrize("body", [
    "See [[stressor:negative-voltage-to-ground]].",
    "See [[stressors/no-such-stressor]].",
    "See [[gadgets/pid]].",
    "See [[pid]].",
])
def test_body_wikilinks_must_resolve(tmp_path, body):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P", body)
    assert ("body-links", "fm:probe", None) in hits(root)


def test_body_wikilink_with_label_resolves(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P",
                 "Like [[failure-modes/pid|PID]] and [[detection-methods/el-imaging]].")
    assert not {r for r, rid, _ in hits(root) if rid == "fm:probe"}


def test_public_body_link_into_overlay(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    overlay = copy_fixture(tmp_path, "overlay")
    write_record(root, "failure-modes", "probe", "id: fm:probe\ntype: FailureMode\nname: P",
                 "Seen in [[cases/wo-1001]].")
    assert ("layers", "fm:probe", None) in hits(root, overlay)
