# Changelog

## Unreleased

- Track A, from a live test of every lab on a free Groq key (gpt-oss-20b):
  - `agent.py` calls the model through `llm.chat`, so the agent's tokens reach `usage.csv` (A8 cost report) and short
    provider errors are retried; if the provider still fails, the agent hands off instead of crashing.
  - `llm.chat` no longer retries a wrong or missing key (401/403).
  - `evaluate.py` and `prompt_test.py` ignore look-alike dashes and spaces in replies, so checks such as `10:00` or a
    leaked `2026-11-04` match however the model types them, and the guardrail's phone mask catches numbers typed
    with non-breaking hyphens (they slipped through unmasked).
  - `evaluate.py` can test the running service: set `EVAL_URL` (A9 rollback drill).
  - `app.py` keeps library request lines out of `requests.log`; `.dockerignore` also excludes `eval_results.csv`.
  - New `templates/mcp-permissions.md` (A6). Setup: Python 3.11 to 3.13 and Node.js; A8 uses the pinned
    `requirements.txt` (no `pip freeze`) and notes free-tier costs; A1, A6 and A9 point to their templates.

## v1.0.0

- First release of the course labs: Start Here, Tracks A, B and C, and the Law and Medical industry packs.
- Track A starter project with pinned library versions (`mcp` below 2) and offline tests.
