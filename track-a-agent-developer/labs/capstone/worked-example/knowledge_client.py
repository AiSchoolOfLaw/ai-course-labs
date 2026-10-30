# knowledge_client.py: lets the A5 agent call the MCP server's search tool
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = StdioServerParameters(command='python', args=['server.py'])

async def _call(name, args):
    async with stdio_client(SERVER) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(name, args)
            return [c.text for c in result.content if c.type == 'text']

def search_knowledge(question, k=3):
    return asyncio.run(_call('search_knowledge', {'question': question, 'k': k}))
