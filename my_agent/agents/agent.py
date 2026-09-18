from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

from .subAgent_math import math_agent
from agents.schemas.schemas import Root_Agent_Output_Schema

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='root agent for the routing of user requests to sub agents',
    instruction="""
    Talk to the user, analyze the incoming request, and manage the conversation flow.
    If the request involves mathematical operations, calculations, or logic problems, delegate the task to math_agent.
    """,
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(include_thoughts=True, thinking_budget=512)
    ),
    output_schema=Root_Agent_Output_Schema,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.45,
        safety_settings=[types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        )]
    ),
    sub_agents=[math_agent],
)