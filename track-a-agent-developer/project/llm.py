import os, json, time, csv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ['LLM_API_KEY'],
                base_url=os.environ.get('LLM_BASE_URL'))  # any OpenAI-compatible provider
MODEL = os.environ.get('MODEL', 'your-model-name')

def chat(messages, attempts=4, **kwargs):
    wait = 1
    for n in range(attempts):
        try:
            resp = client.chat.completions.create(
                model=MODEL, messages=messages, timeout=30, **kwargs)
            log_usage(resp)
            return resp
        except Exception as err:
            if n == attempts - 1:
                raise
            time.sleep(wait)
            wait *= 2  # 1s, 2s, 4s between tries

def log_usage(resp):
    u = resp.usage
    with open('usage.csv', 'a', newline='') as f:
        csv.writer(f).writerow([time.strftime('%Y-%m-%d %H:%M:%S'),
                                u.prompt_tokens, u.completion_tokens])

def ask_json(system, user, required_keys):
    messages = [
        {'role': 'system', 'content': system + ' Reply with JSON only.'},
        {'role': 'user', 'content': user},
    ]
    # If your model does not support response_format, remove it;
    # the key check below still protects you.
    resp = chat(messages, response_format={'type': 'json_object'})
    data = json.loads(resp.choices[0].message.content)
    missing = [k for k in required_keys if k not in data]
    if missing:
        raise ValueError(f'Missing keys: {missing}')
    return data
