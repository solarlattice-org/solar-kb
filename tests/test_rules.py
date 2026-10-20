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


# --- Plan 4d: FaultCode and EventConcept rules (schema 0.4.0) -------------------------------------------------------
FC_SLUG = "chint-sca-50-60ktl-probe90"
FC_FRONT = """id: fc:chint-sca-50-60ktl-probe90
type: FaultCode
name: CPS SCA50-60KTL Probe0090
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Probe0090
code_key: probe90
"""
FC_CITE = '    cite: [{src: "src:chint-fault-manual", loc: "tbl=3.r2", h: "1a2b3c4d5e6f"}]\n    review: drafted\n'
DEFINED_IN = "  - claim_id: c1\n    rel: defined_in\n    target: src:chint-fault-manual\n" + FC_CITE
DERATE = "  - claim_id: c2\n    rel: has_production_effect\n    target: ec:derate\n" + FC_CITE
OUTPUT_LIMIT = ("  - claim_id: c3\n    attr: output_limit\n    value: {max: 50, unit: unit:PERCENT}\n"
                "    conditions: basis=rated_power; while the fan fault persists\n" + FC_CITE)
RECOVERY = "  - claim_id: c4\n    rel: has_recovery\n    target: ec:manual-reset\n" + FC_CITE
RECOVERY_2 = "  - claim_id: c5\n    rel: has_recovery\n    target: ec:service-required\n" + FC_CITE


def fault_code(root, front=FC_FRONT, claims=DEFINED_IN, body="", slug=FC_SLUG):
    write_record(root, "fault-codes", slug, front + "claims:\n" + claims, body)


def fc_rules(root, rid="fc:" + FC_SLUG):
    return {r for r, x, _ in hits(root) if x == rid}


def test_fixture_fault_codes_pass_and_a_minimal_record_is_clean(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, body="<!-- review notes: nothing to add -->\n")
    assert fc_rules(root) == set()


@pytest.mark.parametrize("front, message", [
    (FC_FRONT.replace("code_key: probe90", "code_key: probe0090"), "code_key must be 'probe90'"),
    (FC_FRONT.replace("make_name: CPS\n", ""), "missing required slot(s): make_name"),
    (FC_FRONT + "display_message: one two three four five six seven eight nine\n", "display_message exceeds 8"),
])
def test_fault_code_slot_clauses(tmp_path, front, message):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, front=front)
    found = [v for v in run_rules(load_corpus(root)) if v.record_id == "fc:" + FC_SLUG and v.rule == "fault-code"]
    assert found and any(message in v.message for v in found)


def test_fault_code_id_is_recomputed_from_the_slots(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    front = FC_FRONT.replace("id: fc:chint-sca-50-60ktl-probe90", "id: fc:chint-sca-36ktl-probe90")
    fault_code(root, front=front, slug="chint-sca-36ktl-probe90")  # a wrong family in the id
    found = [v.message for v in run_rules(load_corpus(root)) if v.record_id == "fc:chint-sca-36ktl-probe90"]
    assert any("id must be fc:chint-sca-50-60ktl-probe90" in m for m in found)


def test_fault_code_vendor_severity_and_display_message_word_caps(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, front=FC_FRONT + "vendor_severity: one two three four\n"
                                      "display_message: one two three four five six seven eight\n")
    found = [v.message for v in run_rules(load_corpus(root)) if v.record_id == "fc:" + FC_SLUG]
    assert any("vendor_severity" in m for m in found) and not any("display_message" in m for m in found)


@pytest.mark.parametrize("body, bad", [("Some drafted prose.\n", True), ("<!-- review notes -->\n\n", False), ("", False)])
def test_fault_code_body_is_empty_apart_from_html_comments(tmp_path, body, bad):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, body=body)
    assert ("fault-code" in fc_rules(root)) is bad


@pytest.mark.parametrize("claims, rules", [
    (DEFINED_IN.replace("review: drafted", "quote: never on a code\n    review: drafted"), {"fault-code"}),
    (DEFINED_IN.replace("review: drafted", "note: " + " ".join(["w"] * 26) + "\n    review: drafted"), {"fault-code"}),
    (DEFINED_IN.replace("review: drafted", "conditions: " + " ".join(["w"] * 26) + "\n    review: drafted"),
     {"fault-code"}),
    (RECOVERY, {"fault-code"}),                                                   # no defined_in at all
    (DEFINED_IN.replace("tbl=3.r2", "p=12"), {"fault-code"}),                      # defined_in cites a page
    (DEFINED_IN.replace("tbl=3.r2", "sec=4.3"), {"fault-code"}),                   # or a numbered section
    (DEFINED_IN.replace("tbl=3.r2", "sec=h7"), set()),                             # a heading unit is fine
    (DEFINED_IN.replace("tbl=3.r2", "tbl=3"), set()),                              # so is a whole table (promoted row)
    (DEFINED_IN.replace("target: src:chint-fault-manual", "target: src:sma-core1-manual"), {"fault-code"}),  # cite != target
    (DEFINED_IN + DEFINED_IN.replace("c1", "c2"), {"fault-code"}),                   # two defined_in claims for one source
    (DEFINED_IN + DEFINED_IN.replace("c1", "c2").replace("src:chint-fault-manual", "src:sma-core1-manual"), set()),
    (DEFINED_IN + OUTPUT_LIMIT, {"fault-code"}),                                   # output_limit without ec:derate
    (DEFINED_IN + DERATE + OUTPUT_LIMIT.replace("basis=rated_power; ", ""), {"fault-code"}),  # no basis=
    (DEFINED_IN + DERATE + OUTPUT_LIMIT.replace("basis=rated_power", "basis=curve"), {"fault-code"}),
    (DEFINED_IN + DERATE + OUTPUT_LIMIT, set()),
    (DEFINED_IN + OUTPUT_LIMIT.replace("attr: output_limit", "attr: typical_power_loss"), {"fault-code"}),
    (DEFINED_IN + RECOVERY + RECOVERY_2, {"fault-code"}),                          # two claims on one axis
    (DEFINED_IN + RECOVERY + RECOVERY_2.replace("review: drafted", "conflicts_with: ['fc:chint-sca-50-60ktl-probe90#c4']\n    review: disputed"), set()),
    (DEFINED_IN + "  - claim_id: c2\n    rel: has_recovery\n    target: ec:fault\n" + FC_CITE, {"event-axes"}),
    (DEFINED_IN + "  - claim_id: c2\n    rel: has_event_class\n    target: ec:trip\n" + FC_CITE, {"event-axes"}),
    (DEFINED_IN + "  - claim_id: c2\n    rel: has_production_effect\n    target: ec:auto-reset\n" + FC_CITE,
     {"event-axes"}),
    (DEFINED_IN + "  - claim_id: c2\n    rel: affects\n    target: comp:dc-cable\n" + FC_CITE, set()),  # widened
    (DEFINED_IN + "  - claim_id: c2\n    rel: mitigated_by\n    target: mit:pid-recovery\n" + FC_CITE, set()),
    (DEFINED_IN + "  - claim_id: c2\n    rel: detected_by\n    target: method:el-imaging\n" + FC_CITE, set()),
    (DEFINED_IN + "  - claim_id: c2\n    rel: presents_as\n    target: symptom:ground-fault\n" + FC_CITE, {"targets"}),
])
def test_fault_code_claim_clauses(tmp_path, claims, rules):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, claims=claims)
    assert fc_rules(root) == rules


@pytest.mark.parametrize("extra, bad", [
    ("code_from: 10\n", True),                                   # from without to
    ("code_from: 20\ncode_to: 10\n", True),                      # from >= to
    ("code_from: 10\ncode_to: 20\n", True),                      # Probe0090 is not a printed range
])
def test_fault_code_range_bounds_on_a_single_code(tmp_path, extra, bad):
    root = copy_fixture(tmp_path, "mini")
    fault_code(root, front=FC_FRONT + extra)
    assert ("fault-code" in fc_rules(root)) is bad


@pytest.mark.parametrize("bounds, message", [
    ("code_from: 10\ncode_to: 20\n", None),
    ("code_from: 10\ncode_to: 21\n", "must be the printed range bounds (10, 20)"),
    ("", "a printed range needs code_from and code_to (10, 20)"),  # else containment lookup can never find it
    ("code_from: 10\n", "come together"),
])
def test_fault_code_range_record(tmp_path, bounds, message):
    root = copy_fixture(tmp_path, "mini")
    front = (FC_FRONT.replace("probe90", "probe10-20").replace("code: Probe0090", "code: Probe0010-0020")
             .replace("name: CPS SCA50-60KTL Probe0090", "name: CPS SCA50-60KTL Probe0010-0020") + bounds)
    fault_code(root, front=front, slug="chint-sca-50-60ktl-probe10-20")
    found = [v.message for v in run_rules(load_corpus(root)) if v.record_id == "fc:chint-sca-50-60ktl-probe10-20"]
    assert found == [] if message is None else any(message in m for m in found)


@pytest.mark.parametrize("code, key", [("CRIT-4", "crit4"), ("OV-G-V", "ovgv"), ("Protect0090", "protect90")])
def test_fault_code_hyphenated_single_codes_take_no_bounds(tmp_path, code, key):
    """A dash in the printed code does not make it a range: only parse_code's number_end does (CRIT-4 is number 4 under
    prefix crit). Bounds on such a code would make resolve_code match every number in between."""
    root = copy_fixture(tmp_path, "mini")
    front = (FC_FRONT.replace("probe90", key).replace("code: Probe0090", f"code: {code}")
             .replace("name: CPS SCA50-60KTL Probe0090", f"name: CPS SCA50-60KTL {code}") + "code_from: 1\ncode_to: 999\n")
    fault_code(root, front=front, slug=f"chint-sca-50-60ktl-{key}")
    found = [v.message for v in run_rules(load_corpus(root)) if v.record_id == f"fc:chint-sca-50-60ktl-{key}"]
    assert any("only for a printed range" in m for m in found)


def test_reports_from_a_failure_mode_and_event_concept_with_claims(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    claim_record(root, "  - claim_id: c1\n    rel: reports\n    target: symptom:uniform-power-loss\n" + CITE)
    write_record(root, "event-concepts", "probe", "id: ec:probe\ntype: EventConcept\nname: Probe\naxis: recovery\n"
                 "claims:\n  - claim_id: c1\n    rel: has_recovery\n    target: ec:manual-reset\n" + CITE)
    found = hits(root)
    assert ("targets", "fm:probe", "c1") in found
    assert ("event-axes", "ec:probe", None) in found


def test_fault_code_rules_survive_garbage_shapes(tmp_path):
    root = copy_fixture(tmp_path, "mini")
    write_record(root, "fault-codes", "garbage", "id: fc:garbage\ntype: FaultCode\nname: G\nmake: [1]\ncode: 5\n"
                 "code_key: {a: 1}\ncode_from: x\ncode_to: 3\ndisplay_message: 7\nclaims:\n  - claim_id: c1\n"
                 "    rel: defined_in\n    cite: [{loc: 3}, nope]\n    note: [1]\n  - attr: output_limit\n"
                 "    conditions: 5\n    cite: nope\n")
    write_record(root, "event-concepts", "garbage", "id: ec:garbage\ntype: EventConcept\nname: G\naxis: 3\nclaims: 5")
    run_rules(load_corpus(root))  # must not raise
