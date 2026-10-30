# A5. Tools, Frameworks and Multi-Agent Workflows

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (2 to 3 hours)

Create `agent.py`:

> Code: `project/agent.py`

Then:

1. Run it. Confirm the booking appears in `BOOKINGS` and the advice request is handed off.
2. Try five more inputs: wrong date, a full slot, a caller who will not give a name, a rude caller, a double booking request.
3. Add a fourth tool, `cancel_appointment(name, date, time)`, with a description that says to confirm first.
4. Draw the flow of your agent on paper: request, tool call, result, reply, handoff.
5. Optional multi-agent step: add a second model call that reads the first agent's final reply and answers only APPROVE or REJECT against your rules. Return the reply only if approved.

**Industry pack.** Your industry pack may add one extra tool (for example, a check the business must run before booking). Add it to `TOOLS` and `REGISTRY` the same way.
