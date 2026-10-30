# A3. Prompt and Context Engineering

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (90 minutes)

Create `prompt_test.py`:

> Code: `project/prompt_test.py`

1. Run it and record the score.
2. Extend `CASES` to at least 20 cases, including rude, confusing and off-topic inputs.
3. Make one change to the system prompt (call it `SYSTEM_V2`), rerun and compare scores.
4. Repeat once more. Keep a table: version, change made, score.

**Industry pack.** Your industry pack gives a ready-made set of industry test cases in the same Python format. Run them against your prompt after the core cases pass.

Keyword checks are simple. They catch obvious failures but cannot judge quality; in A7 you will add stronger evaluation.
