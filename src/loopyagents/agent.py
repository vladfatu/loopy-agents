import threading
import time
from smolagents.agents import ToolCallingAgent

class LoopyAgent(ToolCallingAgent):
    def __init__(self, tools: list, loop_delay: float = 1.0, **kwargs):
        super().__init__(tools=tools, **kwargs)
        self.loop_delay = loop_delay
        self.running = False
        self.current_action_thread: threading.Thread | None = None
        self.current_action_name: str | None = None
        self.state: dict = {}

    def start(self, initial_state: dict | None = None):
        self.running = True
        self.state = initial_state or {}
        while self.running:
            # # Build a fresh prompt including tool annotations and current state
            # prompt = self._build_prompt(self.state)

            # # ToolCallingAgent already knows how to decide and return a tool call
            # next_action = self.step(prompt)

            # # Handle thread switching
            # self._maybe_switch_action(next_action, self.state)

            print(f"Running LoopyAgent with state: {self.state}")
            time.sleep(self.loop_delay)

    def stop(self):
        self.running = False