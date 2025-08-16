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



from PIL import Image

# List of local image paths
image_paths = [
    "kitchen_on_fire.jpeg",
]

images = []
for path in image_paths:
    image = Image.open(path).convert("RGB")
    images.append(image)

result = agent.run("What can you see in the image?", images=images)
print(result)