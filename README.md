# SolarSage - RAG Assistant for Solar PV Fault Diagnosis

Ask questions about solar panel faults, diagnostics and maintenance in plain English; get answers grounded in a curated technical corpus, with sources cited. Companion project to [ClaraSol](https://github.com/akshaymehay28/ClaraSol_project) - ClaraSol detects faults from live plant data, SolarSage explains what to do about them.

![CI](https://github.com/akshaymehay28/solarsage/actions/workflows/ci.yml/badge.svg)

## How it works

```
22 technical docs ──► chunker ──► TF-IDF / LSA / hybrid index
                                        │
User question ──► /ask or UI ──► retrieve top-k chunks ──► LLM (Claude, optional)
                                        │                        │
                                        └── extractive fallback ◄┘
                                                   │
                                        answer + cited sources
```

Three interchangeable retrieval strategies share one interface: sparse lexical TF-IDF, dense semantic LSA (truncated SVD over TF-IDF, so paraphrased queries can match without shared keywords), and a weighted hybrid. The API and UI select one at runtime; the eval harness compares all three. Generation uses Claude when `ANTHROPIC_API_KEY` is set and falls back to returning the most relevant passages verbatim otherwise - the system is fully runnable with zero API keys.

## Corpus

22 original documents (about 5,000 words) covering the solar O&M domain: PID, soiling and cleaning, hot spots and bypass diodes, inverter failure modes, ground and arc faults, module cracking and delamination, connector faults, IV curve tracing, IR thermography, EL imaging, degradation mechanisms (LID/LeTID), clipping, shading, snow, weather sensor quality, trackers, preventive maintenance, safety, commissioning, and alarm triage.

## Evaluation

Retrieval measured as hit-rate@k over 42 labelled questions (a hit means the labelled document appears in the top k):

| retriever | hit@1 | hit@3 | hit@5 |
|-----------|-------|-------|-------|
| tfidf     | 88.1% | 95.2% | 97.6% |
| lsa       | 88.1% | 95.2% | 97.6% |
| hybrid    | 88.1% | 95.2% | 97.6% |

Two honest observations from these numbers. First, on a corpus this size with topically distinct documents, semantic retrieval does not beat lexical retrieval - the questions naturally share vocabulary with the documents. LSA's advantage appears on paraphrased queries ("dirt building up on the glass" finding the soiling document without the word "soiling"), which is covered by a dedicated test but underrepresented in the eval set. Second, inspecting the k=1 misses shows most are near-misses where the retrieved document also legitimately covers the topic (morning insulation-resistance trips appear in both the inverter and ground-fault documents), so single-label hit-rate understates real quality. Both are documented limitations of the eval, not surprises discovered later.

Run it yourself: `PYTHONPATH=src python -m eval.run_eval` (also runs in CI on every push).

## Quick start

```bash
pip install -r requirements.txt
pytest                                     # 10 tests
PYTHONPATH=src python -m eval.run_eval     # retriever comparison
PYTHONPATH=src streamlit run streamlit_app.py            # web UI
PYTHONPATH=src uvicorn solarsage.api:app --reload        # JSON API
curl "localhost:8000/ask?q=Why+does+my+inverter+flatten+at+noon?"
```

Environment variables: `ANTHROPIC_API_KEY` enables LLM answers; `RETRIEVER=tfidf|lsa|hybrid` selects the API's strategy (default hybrid).

Or with Docker:

```bash
docker build -t solarsage . && docker run -p 8000:8000 solarsage
```

## Project structure

```
src/solarsage/     ingest.py (chunking) · retrieval.py (3 strategies) ·
                   generate.py (LLM + fallback) · api.py (FastAPI)
streamlit_app.py   web front end
data/docs/         22-document corpus
eval/              42 labelled questions + hit-rate@k comparison harness
tests/             pytest suite (runs in CI)
```

## What I learned

Measuring retrieval separately from generation was the most useful decision in the project: it made every corpus and chunking change quantifiable, and it surfaced the fact that "better" retrieval methods only pay off when queries stop sharing vocabulary with documents. Chunk size is a real trade-off - 800 characters with 150 overlap keeps most sections intact while staying small enough that top-4 retrieval fits comfortably in an LLM context window. Grounded generation needs an explicit contract: the system prompt instructs the model to answer only from context and say so when the context is insufficient, which is the main defence against hallucinated maintenance advice - exactly where a wrong answer could be dangerous. Finally, a labelled eval set is never neutral: writing the questions myself meant they inherited the documents' vocabulary, which is why the paraphrase behaviour needed separate tests.

## Licence

MIT
