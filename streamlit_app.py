"""SolarSage Streamlit front end.

Run locally:  PYTHONPATH=src streamlit run streamlit_app.py
Deployable directly on Streamlit Community Cloud.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

from solarsage.generate import generate_answer
from solarsage.ingest import load_corpus
from solarsage.retrieval import make_retriever

DOCS_DIR = Path(__file__).parent / "data" / "docs"

st.set_page_config(page_title="SolarSage", layout="centered")
st.title("SolarSage")
st.caption(
    "Ask about solar PV faults, diagnostics and maintenance. Answers are "
    "grounded in a curated technical corpus, with sources cited."
)


@st.cache_resource
def get_retriever(name: str):
    return make_retriever(name, load_corpus(DOCS_DIR))


with st.sidebar:
    retriever_name = st.radio("Retrieval strategy", ["hybrid", "tfidf", "lsa"], index=0)
    k = st.slider("Chunks to retrieve", 2, 8, 4)
    st.markdown("---")
    st.markdown(
        "Set `ANTHROPIC_API_KEY` in the environment (or Streamlit secrets) "
        "for LLM-generated answers; otherwise the most relevant passages "
        "are shown directly."
    )

question = st.text_input(
    "Question",
    placeholder="e.g. Why does my inverter output flatten at noon?",
)

if question.strip():
    retriever = get_retriever(retriever_name)
    results = retriever.retrieve(question, k=k)
    response = generate_answer(question, results)

    st.markdown("### Answer")
    st.write(response["answer"])
    st.caption(f"Mode: {response['mode']} | Retriever: {retriever_name}")

    st.markdown("### Sources")
    for r in results:
        with st.expander(f"{r.chunk.doc_id} (chunk {r.chunk.chunk_id}, score {r.score:.3f})"):
            st.write(r.chunk.text)
