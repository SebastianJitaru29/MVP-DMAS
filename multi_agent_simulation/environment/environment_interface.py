from abc import ABC, abstractmethod

class EnvironmentInterface(ABC):

    @abstractmethod
    def add_agent(self, agent):
        """Add an agent to the environment"""
        pass

    @abstractmethod
    def step(self):
        """Move all agents in the environment"""
        pass