# Setup

## Everyone

- A free GitHub account.
- Git: https://git-scm.com/downloads
- A spreadsheet tool and any free AI chat tool.

## Track A (Agent Developer)

1. **Python 3.11 or newer** from https://www.python.org/downloads/.
   On Windows, tick "Add python.exe to PATH" during install.
2. **Visual Studio Code** from https://code.visualstudio.com/, with the Python extension.
3. **Docker Desktop** (needed from A8) from https://www.docker.com/products/docker-desktop/.
4. In a terminal, inside your copy of this repository:

```bash
cd track-a-agent-developer
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example project/.env  # Windows: copy ..\.env.example project\.env
pytest                           # checks your setup; no API key needed
```

5. Put your free API key in `project/.env` (see `providers.md`), then run `python test_llm.py` inside `project/`.

## Track C (Systems Administrator)

- An Azure free account and the Azure CLI: https://learn.microsoft.com/cli/azure/install-azure-cli
- Set a budget alert on day one (C5) and delete resources at the end of each lab.
