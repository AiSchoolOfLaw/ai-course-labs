# A8. Deployment, Version Control, Monitoring and Cost

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (3 hours)

**Part 1: Git (30 minutes).**

You already have a Git repository: your own copy of the course template. Do not run `git init`.

1. Check `.gitignore`. It is in the top folder of your repository (`../../.gitignore` from `project/`) and must list
   `.env`, `.venv/`, `__pycache__/`, `db/`, `usage.csv` and `requests.log`. The template already lists them. If you
   removed any, add them back. This command adds only the lines that are missing:

   ```bash
   for p in .env .venv/ __pycache__/ db/ usage.csv requests.log; do
     grep -qxF "$p" ../../.gitignore || echo "$p" >> ../../.gitignore
   done
   ```

2. Run `git status`. Confirm it does not list `.env`. If it does, stop and fix `.gitignore` before you commit anything.

3. Commit your work, tag it as your first release and start a branch:

   ```bash
   git add . ../../.gitignore
   git commit -m "Initial agent, RAG, MCP server and evaluation"
   git tag v1.0.0
   git checkout -b feature/health-endpoint
   ```

   `v1.0.0` is your first release. It matches the `booking-agent:1.0.0` image you build in Part 3.
   If Git says `tag 'v1.0.0' already exists`, your copy came with the course's own tags (you cloned or forked the
   course repo instead of using the template). Run `git tag -d v1.0.0`, then `git tag v1.0.0` again.

Check again before every later commit: `git status` must never list `.env`.

**Part 2: Web service (60 minutes).** Create `app.py`:

> Code: `project/app.py`

Run `uvicorn app:app --reload`, then open `http://127.0.0.1:8000/docs`. Try `/health` and send three messages to `/chat`. Open `requests.log` and confirm phone numbers and emails are masked.

**Part 3: Docker (45 minutes).** Create `requirements.txt` with `pip freeze > requirements.txt`, then create `Dockerfile`:

> Code: `project/Dockerfile`

Create `.dockerignore` containing `.env`, `.venv` and `db`. Then:

```bash
docker build -t booking-agent:1.0.0 .
docker run --env-file .env -p 8000:8000 booking-agent:1.0.0
```

The key is passed at run time with `--env-file`, so it never sits inside the image.

**Part 4: Cost report (45 minutes).** Create `cost_report.py`:

> Code: `project/cost_report.py`

1. Run your 50-case evaluation set once and then run `cost_report.py`.
2. Apply one cost cut from the A8 lesson (for example a shorter system prompt, a smaller model for simple steps, or caching answers to repeated questions).
3. Run the evaluation and cost report again. Record both quality and cost.
4. Merge your branch only if every safety case still passes, then tag it: `git tag v1.1.0`.
5. Build and run the new release as its own image. Set `VERSION = '1.1.0'` in `app.py`, then run `docker build -t booking-agent:1.1.0 .` and `docker run --env-file .env -p 8000:8000 booking-agent:1.1.0`. Check that `/health` shows 1.1.0. You now have two built images, 1.0.0 and 1.1.0; the A9 rollback drill returns to 1.1.0.
