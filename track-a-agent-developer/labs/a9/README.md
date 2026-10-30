# A9. Governance, Model Lifecycle, Incident Response and Rollback

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (2 to 3 hours)

**Part 1: Kill switch (30 minutes).** Add `import os` to the imports at the top of `app.py`. Then update `chat()` so the kill-switch check runs right after the request id is created, because the reply needs `rid`:

```python
@app.post('/chat')
def chat(body: Ask):
    rid = str(uuid.uuid4())  # create the request id first
    if os.environ.get('AGENT_ENABLED', 'true').lower() != 'true':  # kill switch
        return {'request_id': rid, 'reply': 'Our assistant is unavailable. A staff member will contact you shortly.'}
    start = time.time()
    error = None
    try:
        reply = safe_run(run, body.message)
    except Exception as err:
        error = type(err).__name__
        reply = 'Sorry, something went wrong. A staff member will contact you.'
    ms = round((time.time() - start) * 1000)
    logging.info(json.dumps({
        'time': time.strftime('%Y-%m-%dT%H:%M:%S'), 'request_id': rid,
        'version': VERSION, 'latency_ms': ms, 'error': error,
        'message': mask_pii(body.message)[:200],
    }))
    return {'request_id': rid, 'reply': reply}
```

Restart with `AGENT_ENABLED=false` in `.env` and confirm every message gets the safe reply. Set it back to `true`.

**Part 2: Rollback drill (45 minutes).**

1. Make a deliberately bad release: change the system prompt to remove the professional-advice rule. Commit, tag `v1.2.0`, build `booking-agent:1.2.0`, run it.
2. Run `evaluate.py` and confirm safety cases fail.
3. Stop the container and start the previous image: `docker run --env-file .env -p 8000:8000 booking-agent:1.1.0`.
4. Run `evaluate.py` again and confirm the safety cases pass.
5. Revert the bad commit in Git: `git revert <commit id>`.
6. Record the time from "failure found" to "safe version running". Target: under 15 minutes.

**Part 3: Incident simulation (60 minutes, with a partner).** Your partner plays the client's manager and reports: *"A customer says the assistant read out another customer's phone number."* Work through the six-step routine aloud. Decide the severity, contain, write the notification message, search `requests.log` for the cause, add a test case, and complete the post-incident report.

**Part 4: Model card and drift check (45 minutes).** Complete the model card below for your agent. Then pick 20 entries from `requests.log`, score each pass or fail, and record the rate.

**Industry pack.** For A9, your industry pack has the incident role-play brief and a sample model card for its client.
