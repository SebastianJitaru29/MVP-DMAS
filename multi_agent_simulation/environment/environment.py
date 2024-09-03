from multi_agent_simulation.environment.environment_interface import EnvironmentInterface
class Environment(EnvironmentInterface):
    def __init__(self, size):
        self.size = size
        self.agents = []
        self.obstacles = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        for agent in self.agents:
            agent.move()

            