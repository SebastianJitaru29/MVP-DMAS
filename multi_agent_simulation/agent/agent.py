from multi_agent_simulation.agent.agent_interface import AgentInterface
import numpy as np
class Agent(AgentInterface):
    def __init__(self, x, y, environment, color):
        self.x = x
        self.y = y
        self.environment = environment
        self.color = color

    def move(self):
        direction = np.random.choice(["up", "down", "left", "right"])

        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < self.environment.size - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < self.environment.size - 1:
            self.x += 1

   