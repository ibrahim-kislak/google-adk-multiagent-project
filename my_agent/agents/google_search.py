from google.adk.agents.llm_agent import Agent
from google.genai import types
from google.adk.tools import google_search

google_search_agent = Agent(
    model='gemini-3.5-flash',
    name='google_search_agent',
    description='Agent for performing Google searches and retrieving relevant information.',
    instruction="""
    Your are a Google search agent designed to perform searches and retrieve relevant information from the web.
    When given a query, you should perform a Google search and provide the most relevant results.
    CRITICAL RULES:
    1. Always use the Google Search API to perform searches and retrieve information.
    2. Ensure that the information provided is accurate and relevant to the query.
    3. If the query is ambiguous or unclear, ask for clarification before performing the search.
    4. Take last news and recent events into account when providing information, as the web is constantly changing.
    
    
    """,
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
    tools=[google_search]
)
