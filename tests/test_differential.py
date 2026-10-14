import pytest


def test_differential_tie_breaks_alphabetically_and_returns_discriminators(mini_graph):
    result = mini_graph.differential(["symptom:uniform-power-loss"])
    assert [c["id"] for c in result["candidates"]] == ["fm:pid", "fm:soiling"]
    pairs = {(d["source"], d["target"]) for d in result["discriminators"]}
    assert pairs == {("fm:pid", "fm:soiling"), ("fm:soiling", "fm:pid")}
    assert result["discriminators"][0]["by"] == "method:el-imaging"
    assert result["discriminators"][0]["by_tool_ids"] == ["el-image-analyzer"]
    assert result["kb_version"] == "test-1"


def test_differential_counts_measurements_reached_through_symptoms(mini_graph):
    result = mini_graph.differential(["symptom:uniform-power-loss", "meas:el-negative-end-darkening"])
    top = result["candidates"][0]
    assert top["id"] == "fm:pid" and top["score"] == 2 and top["unmatched"] == []
    assert result["candidates"][1] == {
        "id": "fm:soiling", "name": "Soiling", "score": 1,
        "matched": ["symptom:uniform-power-loss"], "unmatched": ["meas:el-negative-end-darkening"],
        "field_evidence": 0,
        "support": [{"observation": "symptom:uniform-power-loss",
                     "claims": [{"record_id": "fm:soiling", "claim_id": "c1", "review": "drafted"}]}]}


def test_differential_field_evidence_breaks_ties(mini_graph):
    result = mini_graph.differential(
        ["symptom:uniform-power-loss"], field_evidence={("symptom:uniform-power-loss", "fm:soiling"): 5})
    assert [c["id"] for c in result["candidates"]] == ["fm:soiling", "fm:pid"]


def test_differential_review_floor_k_and_unknowns(mini_graph):
    result = mini_graph.differential(
        ["symptom:uniform-power-loss", "symptom:uniform-power-loss", "fm:pid", "free text"],
        min_review="verified", k=1)
    assert [c["id"] for c in result["candidates"]] == ["fm:pid"]
    assert result["discriminators"] == []
    assert result["unknown_observations"] == ["fm:pid", "free text"]


def test_differential_with_no_matches_or_no_input(mini_graph):
    assert mini_graph.differential([])["candidates"] == []
    assert mini_graph.differential(["nonsense"])["unknown_observations"] == ["nonsense"]
    with pytest.raises(ValueError):
        mini_graph.differential(["symptom:uniform-power-loss"], k=0)
