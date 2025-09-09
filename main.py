from agents import Agent,  Runner, function_tool , set_tracing_disabled , enable_verbose_stdout_logging , RunConfig
from decouple import config
from configuration.config import model
from tavily import TavilyClient
import asyncio

set_tracing_disabled(True)
tavily_client = TavilyClient(api_key=config("TAVILY_API_KEY"))

@function_tool
def tavily_search(query: str) -> str:
    """
    Perform a web search using Tavily and return a summarized result.
    """
    response = tavily_client.search(query,search_depth='advanced',max_results='5')
    results = response.get("results", [])
    # print(results["title"])
    return results or "No results found."

async def main():
    agent = Agent(
        name="Web Research Agent",
        instructions="Use tavily_search when you need up-to-date info.",
        tools=[tavily_search],
        model=model
    )
    out = await Runner.run(agent, "what is the current weather in karachi")
    print(out.final_output)
asyncio.run(main())