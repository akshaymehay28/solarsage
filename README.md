# SolarSage 🔆 — RAG Assistant for Solar PV Fault Diagnosis

> Ask questions about solar panel faults and maintenance in plain English; get answers grounded in real technical documentation, with sources cited. Companion project to [ClaraSol](https://github.com/YOUR_USERNAME/clarasol-solar-fault-detection) — ClaraSol *detects* faults, SolarSage *explains what to do about them*.

![CI](https://github.com/YOUR_USERNAME/solarsage/actions/workflows/ci.yml/badge.svg)

## How it works

```
Markdown docs ──► chunker ──► TF-IDF index (baseline, no API key needed)
                                   │
User question ──► /ask ──► retrieve top-k chunks ──► LLM (Claude, optional)
                                   │                        │
                                   └── extractive fallback ◄┘
                                              │
                                   answer + cited sources
```

- **Retrieval**: TF-IDF over overlapping chunks — a deliberate, measurable baseline. Swappable for embeddings.
- **Generation**: if `ANTHROPIC_API_KEY` is set, retrieved context is passed to Claude; otherwise an extractive fallback returns the most relevant passages directly. Fully runnable with zero API keys.
- **Evaluation**: `eval/run_eval.py` measures retrieval hit-rate@k against a labelled question set.

## Quick start

```bash
pip install -r requirements.txt
pytest                              # run tests
PYTHONPATH=src python -m eval.run_eval   # evaluate retrieval
PYTHONPATH=src uvicorn solarsage.api:app --reload
curl "localhost:8000/ask?q=What+causes+PID+in+solar+panels?"
```

Or with Docker:

```bash
docker build -t solarsage . && docker run -p 8000:8000 solarsage
```

## Project structure

```
src/solarsage/     ingest.py (chunking) · retrieval.py (TF-IDF index) ·
                   generate.py (LLM + fallback) · api.py (FastAPI)
data/docs/         source documents (markdown)
eval/              labelled questions + hit-rate@k harness
tests/             pytest suite (runs in CI)
```

## Evaluation results

| Metric | Score |
|--------|-------|
| hit-rate@1 | 100% (8/8) |
| hit-rate@3 | 100% (8/8) |
| hit-rate@5 | 100% (8/8) |

*Seed corpus is small (4 docs, 8 questions), so scores are saturated — the harness exists so scores stay honest as the corpus grows.*

## Roadmap

- [ ] Expand corpus to 20+ real documents (NREL guides, inverter manuals)
- [ ] Embedding-based retrieval + comparison vs TF-IDF baseline in eval
- [ ] Streamlit front end
- [ ] Deploy API on Render

## What I learned

<!-- Fill in as you build: chunk size trade-offs, why measure retrieval
separately from generation, hallucination handling. -->

## Licence

MIT
