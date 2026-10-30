# n8n sample flow (B4)

The n8n hosting decision is still open, so this repo has no exported n8n workflow yet.
Build the flow by hand from the B4 lab steps:

1. Trigger: a new row is added to a spreadsheet (a fake customer message).
2. Action: send the text to an AI step with your best prompt.
3. Condition: if the AI output starts with ESCALATE, write the row to an "Escalations" sheet; otherwise to "Drafts".
4. Error notification to your own email.

Use a free Groq or Gemini key for the AI step. Never export a workflow that contains a key:
n8n stores keys as credentials, which stay out of the workflow file, but check before you commit.
If n8n is not available, use `paper-flow-template.md`.
