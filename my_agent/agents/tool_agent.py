from google.adk.agents import Agent
from .tools.calculatingTools import get_system_datetime, save_quick_note, get_simulated_fx_rate
tool_executor_agent = Agent(
    model="gemini-2.0-flash",
    name="tool_executor_agent",
    description="Agent responsible for executing specific system utilities like checking datetime, saving notes, or currency conversions.",
    instruction="""
You are a tool execution specialist. 
When asked to get the current date/time, save a note, or convert currency, select and execute the appropriate tool from your toolkit and report the outcome clearly.
""",
    tools=[get_system_datetime, save_quick_note, get_simulated_fx_rate],
)