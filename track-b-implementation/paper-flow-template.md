# Paper flow: <flow name>

Use this when no workflow tool (n8n, Power Automate, Zapier or Make) is available. It
counts as your B4 automation in B5 and B6.

| Step | Type (trigger / action / condition / error) | What happens | Tool used (AI chat, spreadsheet) |
| --- | --- | --- | --- |
| 1 | Trigger | A new message arrives (one row in the sample messages) | Spreadsheet |
| 2 | Action | Paste the message and your prompt into the AI chat tool | AI chat |
| 3 | Condition | If the reply starts with ESCALATE, record it in Escalations; otherwise in Drafts | Spreadsheet |
| 4 | Error | If the AI gives no usable reply, tell a named person | Email or chat |

## Run log

| Message ID | Reply starts with ESCALATE? | Sheet (Drafts / Escalations) | Correct? | Notes |
| --- | --- | --- | --- | --- |
