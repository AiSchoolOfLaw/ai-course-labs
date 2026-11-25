# A8. Deployment, Version Control, Monitoring and Cost

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (3 hours)

**Part 1: Git (30 minutes).**

```bash
git init
printf '.env\n.venv/\n__pycache__/\ndb/\nusage.csv\nrequests.log\n' > .gitignore
git add .
git commit -m "Initial agent, RAG, MCP server and evaluation"
git checkout -b feature/health-endpoint
```

Confirm `git status` does not list `.env`. If it does, stop and fix `.gitignore` before you commit anything else.

**Part 2: Web service (60 minutes).** Create `app.py`:

> Code: `project/app.py`

Run `uvicorn app:app --reload`, then open `http://127.0.0.1:8000/docs`. Try `/health` and send three messages to `/chat`. Open `requests.log` and confirm phone numbers and emails are masked.

**Part 3: Docker (45 minutes).** Use the `requirements.txt` that came with your copy of the template: its versions are pinned and tested together. Do not run `pip freeze > requirements.txt`: it copies the exact versions on your computer, which the image's Python 3.11 may not be able to install. The template also has the `Dockerfile`:

> Code: `project/Dockerfile`

Check `.dockerignore`: the template's file already keeps `.env`, `.venv`, `db`, `__pycache__`, `usage.csv`, `requests.log` and `eval_results.csv` out of the image. Then:

```bash
docker build -t booking-agent:1.0.0 .
docker run --env-file .env -p 8000:8000 booking-agent:1.0.0
```

The key is passed at run time with `--env-file`, so it never sits inside the image.

**Part 4: Cost report (45 minutes).** Create `cost_report.py`:

> Code: `project/cost_report.py`

1. Run your 50-case evaluation set once and then run `cost_report.py`. On a free tier your real cost is zero, so fill in `INPUT_PRICE` and `OUTPUT_PRICE` from your provider's paid price list: the report then shows what the same traffic would cost on a paid plan.
2. Apply one cost cut from the list above (for example a shorter system prompt).
3. Run the evaluation and cost report again. Record both quality and cost.
4. Merge your branch only if every safety case still passes, then tag it: `git tag v1.1.0`.
5. Build and run the new release as its own image. Set `VERSION = '1.1.0'` in `app.py`, then run `docker build -t booking-agent:1.1.0 .` and `docker run --env-file .env -p 8000:8000 booking-agent:1.1.0`. Check that `/health` shows 1.1.0. You now have two built images, 1.0.0 and 1.1.0; the A9 rollback drill returns to 1.1.0.
