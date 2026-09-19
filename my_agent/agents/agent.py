from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types
from .google_search import google_search_agent
from .subAgent_math import math_agent
from agents.schemas.schemas import Root_Agent_Output_Schema

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='root agent for the routing of user requests to sub agents',
    instruction="""
    You are the primary orchestrator and conversation manager. Your responsibilities:

    1. GENERAL CONVERSATION & CHIT-CHAT:
    - Handle general greetings, polite exchanges, small talk, questions about your capabilities, and high-level conversational flow directly by yourself. Do NOT delegate simple greetings or chit-chat to sub-agents.

    2. ROUTING & DELEGATION:
    - If the user request requires searching the web, retrieving up-to-date facts, current news, external information, or general web lookup, delegate the task immediately to 'google_search_agent'.
    - If the user request involves mathematical operations, equations, numerical reasoning, or calculations, delegate the task immediately to 'math_agent'.

    3. COORDINATION:
    - Synthesize the responses from sub-agents when necessary and deliver a coherent, clear final response adhering to the defined schema.
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
    sub_agents=[math_agent, google_search_agent],
)