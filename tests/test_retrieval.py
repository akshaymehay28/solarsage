from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from solarsage.api import app
from solarsage.ingest import chunk_text, load_corpus
from solarsage.retrieval import (
    HybridRetriever,
    LsaRetriever,
    TfidfRetriever,
    make_retriever,
)

DOCS = Path(__file__).resolve().parents[1] / "data" / "docs"


def test_chunk_text_overlap_and_coverage():
    text = "word " * 500
    chunks = chunk_text(text, size=200, overlap=50)
    assert len(chunks) > 1
    assert all(len(c) <= 200 for c in chunks)


def test_chunk_text_rejects_bad_params():
    with pytest.raises(ValueError):
        chunk_text("hello", size=100, overlap=100)


def test_corpus_loads():
    corpus = load_corpus(DOCS)
    assert len({c.doc_id for c in corpus}) >= 20
    assert all(c.text for c in corpus)


@pytest.mark.parametrize("cls", [TfidfRetriever, LsaRetriever, HybridRetriever])
def test_retrieval_finds_relevant_doc(cls):
    retriever = cls(load_corpus(DOCS))
    results = retriever.retrieve("What causes potential induced degradation?", k=3)
    assert results[0].score > 0
    assert any("pid" in r.chunk.doc_id for r in results)


def test_lsa_matches_without_shared_keywords():
    # "dirt building up" does not use the word "soiling"
    retriever = LsaRetriever(load_corpus(DOCS))
    results = retriever.retrieve("dirt building up on the glass reduces output", k=5)
    assert any(r.chunk.doc_id in {"soiling_maintenance", "cleaning_methods"} for r in results)


def test_make_retriever_rejects_unknown_name():
    with pytest.raises(ValueError):
        make_retriever("nonsense", load_corpus(DOCS))


def test_api_ask_endpoint():
    client = TestClient(app)
    resp = client.get("/ask", params={"q": "How do I clean soiled panels?"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["mode"] in {"llm", "extractive"}
    assert body["sources"]
    assert body["retriever"] in {"tfidf", "lsa", "hybrid"}


def test_api_rejects_empty_question():
    client = TestClient(app)
    assert client.get("/ask", params={"q": "  "}).status_code == 400
