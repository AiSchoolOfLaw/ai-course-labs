import re

EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
PHONE = re.compile(r'(?<!\d)(?:\+\d{1,3}[\s.-]?)?\(?\d{3,5}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}(?!\d)')  # does not mask dates such as 2026-11-04

def mask_pii(text):
    return PHONE.sub('[PHONE]', EMAIL.sub('[EMAIL]', text))

INJECTION_HINTS = [
    'ignore previous instructions', 'ignore all previous', 'ignore your rules',
    'reveal your system prompt', 'show your system prompt', 'you are now',
]

def looks_like_injection(text):
    t = text.lower()
    return any(h in t for h in INJECTION_HINTS)

def safe_run(agent_run, user_text):
    if looks_like_injection(user_text):
        return 'I cannot help with that request. I will pass you to a staff member.'
    reply = agent_run(user_text)
    return mask_pii(reply)
