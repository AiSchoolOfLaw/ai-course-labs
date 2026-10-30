import csv

# Fill these from your provider's current price page (dollars per 1 million tokens).
INPUT_PRICE = 0.0
OUTPUT_PRICE = 0.0

total_in = total_out = calls = 0
with open('usage.csv') as f:
    for row in csv.reader(f):
        total_in += int(row[1]); total_out += int(row[2]); calls += 1

cost = total_in / 1e6 * INPUT_PRICE + total_out / 1e6 * OUTPUT_PRICE
print(f'Calls: {calls}  Input tokens: {total_in}  Output tokens: {total_out}')
print(f'Total cost: ${cost:.4f}  Average per call: ${cost / max(calls, 1):.5f}')
