# A4. Retrieval-Augmented Generation (RAG)

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (2 hours)

Create `client_docs.py` with fake documents:

> Code: `project/client_docs.py`

Create `rag.py`:

> Code: `project/rag.py`

The first run may download a small embedding model, so you need internet access. Then:

1. Run `python rag.py` and read each answer with its sources.
2. Write 10 test questions: 6 the documents answer, 4 they cannot (for example the manager's name). Record the expected answer for each.
3. Mark each result: right source retrieved? answer correct? For the 4 unanswerable questions, did it refuse?
4. Change `size` and `k`, rerun, and note what changes.
5. Compute: correct-answer rate, correct-refusal rate, retrieval hit rate.

**Industry pack.** Your industry pack gives a `DOCS` dictionary of 10 industry documents and 10 test questions (6 answerable, 4 the assistant must refuse). Swap it in for `client_docs.py`; `rag.py` does not change.

**Free next steps.** The DeepLearning.AI course *Building and Evaluating Advanced RAG* covers sentence-window and auto-merging retrieval and the RAG triad.
