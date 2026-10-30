# Free AI providers for the Track A labs

The labs use the `openai` Python package with any OpenAI-compatible provider. To switch
provider, change only the three lines in `.env`: `LLM_API_KEY`, `LLM_BASE_URL` and `MODEL`.

| Provider | `LLM_BASE_URL` | Key | Best use |
| --- | --- | --- | --- |
| Groq (default) | `https://api.groq.com/openai/v1` | Free at console.groq.com | A2 to A9 |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta/openai/` | Free in Google AI Studio | Backup; use a Flash-Lite model for volume |
| Ollama Cloud | `https://ollama.com/v1` | Free at ollama.com | Backup; open models |
| Ollama on your computer | `http://localhost:11434/v1/` | `ollama` | Unlimited and offline; A7 evaluation runs (needs about 16 GB RAM) |

Set `MODEL` to a model name listed in your provider's console. A full A7 evaluation run can
take about 300 requests, so use Groq or local Ollama for it.

Free limits change often. Check them in the provider's console before each cohort.
