from abc import ABC, abstractmethod

class AgentInterface(ABC):
    @abstractmethod
    def move(self):
        """Move the agent based on its behaviour"""
        pass