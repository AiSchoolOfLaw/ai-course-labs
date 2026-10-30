# From the Track C course (C5 lab). Needs: pip install pandas
import pandas as pd

PRICE_PER_MILLION_TOKENS = 5.0  # price used in this course
df = pd.read_csv('track-c-c5-usage.csv')
by_dept = df.groupby('department').agg(
    active_users=('user', 'nunique'), prompts=('prompts', 'sum'), tokens=('tokens', 'sum'))
by_dept['cost'] = by_dept['tokens'] / 1e6 * PRICE_PER_MILLION_TOKENS
by_dept['prompts_per_user'] = by_dept['prompts'] / by_dept['active_users']
print(by_dept.sort_values('cost', ascending=False))
