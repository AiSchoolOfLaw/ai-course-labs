# A6. Model Context Protocol (MCP)

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### Lab (2 hours)

Create `server.py`:

> Code: `project/server.py`

1. Run `mcp dev server.py`. This should open the MCP Inspector in your browser. If the command differs in your SDK version, follow the current Python SDK documentation.
2. In the Inspector, list the tools, resources and prompts. Call `check_availability` with `2026-11-03`, then with a date that has no slots.
3. Read the `policy://cancellation` resource.
4. Add a second tool, `list_services`, that returns a fixed list.
5. Add input checking to `check_availability`: reject any date that is not in YYYY-MM-DD format.
6. Add logging: write the tool name and arguments to a file on every call.
7. Complete the permissions table below.

**Industry pack.** Expose your industry pack's extra tool or documents from the same MCP server if you added them in A5.

**Free next step.** Anthropic Academy offers free courses on MCP (introduction and advanced topics) with completion certificates.
