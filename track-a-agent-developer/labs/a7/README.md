# A7. Guardrails, Safety and Evaluation

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (2 to 3 hours)

Create `guardrails.py`:

> Code: `project/guardrails.py`

These simple filters are only a first layer. Attackers rephrase. Your evaluation set and the other layers matter more.

Create `evaluate.py`:

> Code: `project/evaluate.py`

1. Run the four starter cases and read the failures.
2. Grow the set to 50 cases using the mix above.
3. For each failure, decide which layer should have stopped it and fix that layer.
4. Rerun until all safety cases (adversarial and sensitive) pass.
5. Write a one-page evaluation report.

**Industry pack.** Use the 50-case evaluation set from your industry pack (20 normal, 10 edge, 10 adversarial, 10 must hand off). It drops into `evaluate.py` in place of the core cases.
