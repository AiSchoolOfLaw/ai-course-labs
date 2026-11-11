# Track A: AI Agent Developer labs

- `project/`: the agent you build across the course. Every lab adds to the same folder.
  The starter files hold the code the course gives you. Lines marked `TODO` are yours to write.
- `labs/`: the steps for each module (A1 to A9 and the capstone).
- `templates/`: the deliverable templates (Agent Specification, reports, model card).
- `tests/`: automatic checks that run without an API key, using a fake AI.

## Start

```bash
cd track-a-agent-developer
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example project/.env  # then put your free API key in project/.env
cd project
python test_llm.py
```

Run the tests at any time from `track-a-agent-developer/`: `pytest`.

## Note for A8 (Git)

You already have a Git repository (your copy of this template), so the A8 lab has no
`git init` step. Part 1 has you check that the top-level `.gitignore` lists `.env`, `.venv/`,
`__pycache__/`, `db/`, `usage.csv` and `requests.log` (add any that are missing), commit your work,
tag it `v1.0.0` (your first release, matching the `booking-agent:1.0.0` image) and create the
`feature/health-endpoint` branch. Part 4 tags the improved release `v1.1.0`. Check that
`git status` never lists `.env`.

## Industry packs

Your industry pack's files are in `../industry-packs/<pack>/track-a/`. They drop into
`project/` in place of the core files (for example `client_docs.py` and the evaluation cases).
