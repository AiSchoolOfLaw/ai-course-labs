# Capstone: Production-Ready Client Agent

Lab steps from the Track A course. Work in `track-a-agent-developer/project/`.
Lines marked TODO in the project files are the parts you write yourself.

### The client

The capstone client comes from **your industry pack** (for example, a law firm in the Law pack or a health clinic in the Medical pack). Whatever the industry, you build a **knowledge assistant for the client's own staff** that:

- answers questions from the client's policies and reference documents, always showing its sources (RAG);
- drafts routine letters or messages from approved templates (tool);
- records an entry (for example a time entry, task or rota change) only after the staff member confirms it (a tool that changes data);
- hands off anything that needs professional judgment to a qualified person.

Every learner in a cohort builds the same capstone from the same industry pack. The pack holds the client brief, document pack, tool specifications, test questions and marker checklist. The requirements and rubric below are the same for every industry.

### Minimum requirements

1. **Agent Specification** approved by the instructor acting as client (A1).
2. **RAG** over the document pack with sources returned on every answer (A4).
3. At least **three tools**, including one that changes data and requires user confirmation (A5).
4. Tools or data exposed through an **MCP server** with input checks and call logging (A6).
5. **Guardrails** on input, tools and output (A7).
6. **Evaluation set of 50 cases** (20 normal, 10 edge, 10 adversarial, 10 sensitive). All safety cases pass; overall pass rate 90% or higher (A7).
7. **FastAPI service in Docker** with `/health`, masked request logs and a kill switch (A8, A9).
8. **Git repository** with tagged releases and a working rollback (A8, A9).
9. **Cost report** with cost per conversation and one tested saving (A8).

### Worked example: one request through RAG, the agent and MCP

The labs build each part on its own. In the capstone they must work as one system. This example follows one question through every layer, using the Example Services files from the labs. Your industry pack's documents replace `client_docs.py`; nothing else changes.

**The flow.**

1. **Input guardrail (A7).** `app.py` receives "What is the late cancellation fee?" and passes it to `safe_run`, which blocks injection attempts.
2. **Agent (A5).** `run()` sends the question, system prompt and tool list to the model. The model decides it needs the business documents and calls `search_knowledge`.
3. **MCP (A6).** The agent's tool function calls the `search_knowledge` tool on your MCP server, which checks the input and logs the call.
4. **RAG (A4).** The server queries the Chroma index built from your documents and returns the top passages, each with its source.
5. **Grounded answer.** The agent sends the passages back to the model, which answers only from them and names the source, for example: "Cancellations later than 24 hours before the visit cost 50 dollars \[cancellation\]."
6. **Output guardrail (A7).** `safe_run` masks any personal data before the reply is returned and logged.

**Step 1: expose search on the MCP server.** Add this to `server.py`, below the existing tools:

> Code: `labs/capstone/worked-example/server_addition.py`

**Step 2: let the agent call the MCP server.** Create `knowledge_client.py`:

> Code: `labs/capstone/worked-example/knowledge_client.py`

**Step 3: give the agent the tool.** Add this to `agent.py`, below `SYSTEM` and `TOOLS`:

> Code: `labs/capstone/worked-example/agent_addition.py`

**Check it.** Ask three questions through `/chat`: one the documents answer (expect a source in brackets), one they do not (expect "I do not have that information"), and one that asks for professional advice (expect a handoff). Add all three to your evaluation set. Starting the MCP server for every call keeps this example short but is slow; in your capstone, keep one session open while the service runs.
