"""Checks every CSV parses with a consistent column count and every eval set has 50 unique ids."""
import csv, glob, importlib.util, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
problems = []

for path in sorted(glob.glob(os.path.join(ROOT, '**', '*.csv'), recursive=True)):
    if '.venv' in path:
        continue
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    widths = {len(r) for r in rows if r}
    rel = os.path.relpath(path, ROOT)
    if not rows or len(widths) != 1:
        problems.append(f'{rel}: inconsistent columns {sorted(widths)}')
    else:
        print(f'ok  {rel}: {len(rows) - 1} rows, {widths.pop()} columns')

for path in sorted(glob.glob(os.path.join(ROOT, 'industry-packs', '*', 'track-a', 'eval_cases_*.py'))):
    spec = importlib.util.spec_from_file_location('cases', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ids = [c['id'] for c in mod.CASES]
    rel = os.path.relpath(path, ROOT)
    if len(ids) != 50 or len(set(ids)) != 50:
        problems.append(f'{rel}: {len(ids)} cases, {len(set(ids))} unique ids')
    else:
        print(f'ok  {rel}: 50 cases, unique ids')

if problems:
    print('\n'.join('FAIL ' + p for p in problems))
    sys.exit(1)
print('All data files valid.')
