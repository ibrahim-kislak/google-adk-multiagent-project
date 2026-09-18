from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltInCodeExecutor
from .schemas.schemas import Math_Agent_Output_Schema
from google.genai import types
math_agent = Agent(
    model='gemini-3.5-flash',
    name='math_agent',
    description='math agent for solving math problems and providing explanations.',
    instruction="""
    You are a math agent designed to solve mathematical problems and provide clear explanations and step by step solutions. 
    You can handle a variety of math topics, including algebra, calculus, geometry, and more.
    When given a problem, you should provide a step-by-step solution and explain the reasoning behind each step. 
    If the problem is complex, break it down into manageable parts and ensure that your explanations are easy to understand for users of all levels.
    CRITICAL RULES:
    1. Never solve complex math or perform calculations mentally in text.
    2. ALWAYS write Python code and use the code_executor to compute and verify all mathematical results.
    3. Ensure all fields in the Output Schema are populated correctly based on the code execution output.
    """,
    code_executor=BuiltInCodeExecutor(),
    output_schema=Math_Agent_Output_Schema,
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
    )
    