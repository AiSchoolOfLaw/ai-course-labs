from mcp.server.fastmcp import FastMCP

mcp = FastMCP('client-demo')

SLOTS = {'2026-11-03': ['09:00', '14:00'], '2026-11-04': ['10:00']}

@mcp.tool()
def check_availability(date: str) -> list[str]:
    """Return open appointment times for a date in YYYY-MM-DD format. Read-only."""
    return SLOTS.get(date, [])

@mcp.resource('policy://cancellation')
def cancellation_policy() -> str:
    """Cancellation policy."""
    return 'Appointments may be canceled up to 24 hours before the visit without charge.'

@mcp.prompt()
def intake_summary(notes: str) -> str:
    """Template for summarizing intake notes."""
    return f'Summarize these intake notes in three bullet points: {notes}'

# TODO (A6 step 4): add a second tool, list_services, that returns a fixed list.
# TODO (A6 step 5): reject any date in check_availability that is not YYYY-MM-DD.
# TODO (A6 step 6): log the tool name and arguments to a file on every call.

if __name__ == '__main__':
    mcp.run()
