from __future__ import annotations

import pytest

from solar_kb.graph import build_graph
from solar_kb.query import Graph
from solar_kb.records import load_corpus
from tests.helpers import FIXTURES


@pytest.fixture
def mini_graph(tmp_path):
    corpus = load_corpus(FIXTURES / "mini")
    db = tmp_path / "graph.sqlite"
    build_graph(corpus, db, kb_version="test-1")
    graph = Graph(db)
    yield graph
    graph.close()
