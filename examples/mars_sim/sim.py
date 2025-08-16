from loopyagents.agent import LoopyAgent
from smolagents.tools import tool
from smolagents.agents import ToolCallingAgent
from smolagents import LiteLLMModel

@tool
def move(direction: str = "forward") -> str:
    """Move the rover in a given direction.
    Args:
        direction (str): The direction to move the rover.
    Returns:
        str: A message indicating the movement.
    """
    print(f"Moving {direction}")
    return f"Moved {direction}"

@tool
def collect_sample() -> str:
    """Collect a dirt sample.

    Returns:
        str: A message indicating the sample collection.
    """
    print("Collecting sample")
    return "Sample collected"

model = LiteLLMModel(model_id="gemini/gemini-2.5-flash-lite")

agent = ToolCallingAgent(tools=[move, collect_sample], model=model)

result = agent.run("What is the third number in the Fibonacci sequence?")
print(result)