# Add to agent.py (A5)
from knowledge_client import search_knowledge

REGISTRY['search_knowledge'] = search_knowledge
TOOLS.append({'type': 'function', 'function': {
    'name': 'search_knowledge',
    'description': 'Search the business documents (hours, policies, services). Read-only. '
                   'Use for any question about how the business works.',
    'parameters': {'type': 'object',
                   'properties': {'question': {'type': 'string'}},
                   'required': ['question']}}})
SYSTEM += (' For questions about the business, call search_knowledge and answer only from the '
           'passages it returns, naming each source in brackets. If no passage answers the '
           'question, reply: I do not have that information.')
