import json
from llm import client, MODEL

SLOTS = {'2026-11-03': ['09:00', '14:00'], '2026-11-04': ['10:00']}
BOOKINGS = []

def check_availability(date):
    return SLOTS.get(date, [])

def book_appointment(name, date, time):
    if time not in SLOTS.get(date, []):
        return {'ok': False, 'reason': 'slot not available'}
    SLOTS[date].remove(time)
    BOOKINGS.append({'name': name, 'date': date, 'time': time})
    return {'ok': True, 'confirmation': f'{name} on {date} at {time}'}

def hand_off_to_human(reason):
    return {'ok': True, 'message': 'A staff member will contact you shortly.', 'reason': reason}

def cancel_appointment(name, date, time):
    """TODO (A5 step 3): cancel a booking after the customer confirms.
    Remove it from BOOKINGS, put the slot back in SLOTS, then add this function
    to REGISTRY and describe it in TOOLS (say that the agent must confirm first)."""
    raise NotImplementedError('A5 step 3: write cancel_appointment')

REGISTRY = {
    'check_availability': check_availability,
    'book_appointment': book_appointment,
    'hand_off_to_human': hand_off_to_human,
}

TOOLS = [
    {'type': 'function', 'function': {
        'name': 'check_availability',
        'description': 'List open appointment times for one date. Read-only.',
        'parameters': {'type': 'object',
                       'properties': {'date': {'type': 'string', 'description': 'YYYY-MM-DD'}},
                       'required': ['date']}}},
    {'type': 'function', 'function': {
        'name': 'book_appointment',
        'description': 'Book one slot. Only call after the caller confirmed name, date and time.',
        'parameters': {'type': 'object',
                       'properties': {'name': {'type': 'string'},
                                      'date': {'type': 'string'},
                                      'time': {'type': 'string'}},
                       'required': ['name', 'date', 'time']}}},
    {'type': 'function', 'function': {
        'name': 'hand_off_to_human',
        'description': 'Pass the customer to staff. Use for professional advice (medical, legal or financial), complaints, or any request outside booking.',
        'parameters': {'type': 'object',
                       'properties': {'reason': {'type': 'string'}},
                       'required': ['reason']}}},
]

SYSTEM = (
    'You are the booking assistant for Example Services. You can check availability and book appointments. '
    'Never give professional advice (medical, legal or financial); hand off instead. Ask for the customer name before booking. Keep replies short.'
)
MAX_STEPS = 6

def run(user_text):
    messages = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': user_text}]
    for step in range(MAX_STEPS):
        resp = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        msg = resp.choices[0].message
        if not msg.tool_calls:
            return msg.content
        messages.append(msg.model_dump(exclude_none=True))  # plain dict works with every provider
        for tc in msg.tool_calls:
            fn = REGISTRY.get(tc.function.name)
            try:
                args = json.loads(tc.function.arguments or '{}')  # inside try: bad JSON must not crash the agent
                result = fn(**args) if fn else {'ok': False, 'reason': 'unknown tool'}
            except (json.JSONDecodeError, TypeError) as err:
                result = {'ok': False, 'reason': f'bad arguments: {err}'}  # the model sees this and can retry
            messages.append({'role': 'tool', 'tool_call_id': tc.id, 'content': json.dumps(result)})
    return hand_off_to_human('step limit reached')['message']

if __name__ == '__main__':
    print(run('Hi, I am Sam Lee. Do you have anything on 2026-11-03? Book the 14:00 please.'))
    print(BOOKINGS)
    print(run('Can you give me your expert advice on my problem?'))
