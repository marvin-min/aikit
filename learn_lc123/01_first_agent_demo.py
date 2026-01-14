from langchain.agents import create_agent
from langchain.tools import tool
from models import get_client

llm = get_client()


@tool
def search(query: str) -> str:
  """Perform a search for the given query and return a formatted result string.

  Args:
    query: The search query to look up.

  Returns:
    A formatted string containing the search results.
  """
  return f"Search results for '{query}': ..."


@tool
def get_weather(location: str) -> str:
  """Return a mock weather summary for a given location.

  Args:
    location: Location to get weather for.

  Returns:
    A short weather summary string.
  """
  return f"The weather in {location} is sunny with a high of 75°F."


agent = create_agent(llm, tools=[search, get_weather])

result = agent.invoke(
  {"messages": [{"role": "user", "content": "芝加哥天气如何?"}]}
)

print(result)