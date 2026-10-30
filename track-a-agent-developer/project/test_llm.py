from llm import ask_json

result = ask_json(
    'Classify the customer message. Return keys: category (booking, billing, other) and urgency (low, high).',
    'Hi, I was charged twice for my visit and need this fixed today.',
    ['category', 'urgency'])
print(result)
