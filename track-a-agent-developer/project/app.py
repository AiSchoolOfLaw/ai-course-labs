import time, uuid, json, logging
from fastapi import FastAPI
from pydantic import BaseModel
from agent import run
from guardrails import safe_run, mask_pii

logging.basicConfig(filename='requests.log', level=logging.INFO, format='%(message)s')
app = FastAPI(title='Booking Agent')
VERSION = '1.0.0'

class Ask(BaseModel):
    message: str

@app.get('/health')
def health():
    return {'status': 'ok', 'version': VERSION}

# TODO (A9 Part 1): add the kill switch. Follow the A9 lab: add `import os`, then check
# AGENT_ENABLED right after the request id is created.
@app.post('/chat')
def chat(body: Ask):
    rid = str(uuid.uuid4())
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
