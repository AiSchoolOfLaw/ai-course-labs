# Extra A5 tool for the Law pack. Add it to agent.py, REGISTRY and TOOLS.
EXISTING_CLIENTS = ['Martin Hale', 'Xena Brooks']

def search_conflicts(name):
    """Read-only. True if the firm already acts for this person."""
    match = name.strip().lower() in [c.lower() for c in EXISTING_CLIENTS]
    return {'match': match}
