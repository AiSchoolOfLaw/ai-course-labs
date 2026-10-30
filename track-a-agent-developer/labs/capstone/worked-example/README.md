# Capstone worked example: one request through RAG, the agent and MCP

These three snippets come from the capstone section of the Track A course. They connect
the parts you built in A4 (RAG), A5 (agent) and A6 (MCP server).

1. Paste `server_addition.py` into `project/server.py`, below the existing tools.
2. Copy `knowledge_client.py` into `project/`.
3. Paste `agent_addition.py` into `project/agent.py`, below `SYSTEM` and `TOOLS`.
4. Ask three questions through `/chat` (one the documents answer, one they do not,
   one that asks for professional advice) and add all three to your evaluation set.

Starting the MCP server for every call keeps the example short but is slow. In your
capstone, keep one session open while the service runs.
