from pydantic import BaseModel, Field
from agents import Agent

AGENT_COUNT=3

INSTRUCTIONS = f"You are a helpful assistant that can help with research. Given a query, come up with a \
    set of web searches to perform to best answer the query. Output {AGENT_COUNT} terms to query for."

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to answer query")

planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)