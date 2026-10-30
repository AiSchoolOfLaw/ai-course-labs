# AI Course Labs

Practice files and starter code for the three AI role courses:

| Folder | Course |
| --- | --- |
| `start-here/` | Start Here: Foundation (everyone does this first) |
| `track-a-agent-developer/` | Track A: AI Agent Developer (Python) |
| `track-b-implementation/` | Track B: AI Implementation Specialist (no code) |
| `track-c-sysadmin/` | Track C: AI Systems Administrator |
| `industry-packs/law/`, `industry-packs/medical/` | Practice data for your industry pack |

## Get your own copy

1. On GitHub, click **Use this template**, then **Create a new repository**. Make it private.
2. Clone your new repository to your computer.
3. Copy `.env.example` to `.env` and put your own free API key in `.env` (Track A only).
4. Track A: follow `track-a-agent-developer/README.md` (`pip install -r requirements.txt`).

Full setup help: `docs/setup.md`. Free AI providers: `docs/providers.md`.

## Free AI providers (Track A)

| Provider | `LLM_BASE_URL` | Notes |
| --- | --- | --- |
| Groq (default) | `https://api.groq.com/openai/v1` | Free key at console.groq.com |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta/openai/` | Free key in Google AI Studio |
| Ollama Cloud | `https://ollama.com/v1` | Free key at ollama.com |
| Ollama on your computer | `http://localhost:11434/v1/` | Set `LLM_API_KEY=ollama`; best for A7 evaluation runs |

Free limits change often. Check yours in the provider's console before you start.

## Safety rules

- Use fake data only. Never put real client, customer, patient or personal data in this repository.
- Never commit `.env`, API keys or passwords. `.gitignore` blocks `.env`; check `git status` before every commit.
- If you commit a key by mistake, delete the key in the provider's console straight away, then tell your instructor.

## Found a problem in a lab?

Open an issue with the "Lab bug" template, or tell your instructor.
