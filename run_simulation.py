import tkinter as tk
from multi_agent_simulation.visualization.visualization import Visualization    
from multi_agent_simulation.environment.environment import Environment
from multi_agent_simulation.agent.agent import Agent
import signal
import sys

def shutdown_simulation(signal, frame):
    print("\nShutting down simulation")
    sys.exit(0)

def main():
    root = tk.Tk()
    root.title("Multi-Agent Simulation")
    
    env = Environment(size=40)
    agent = Agent(x=20, y=20, environment=env, color="red")
    agent2 = Agent(x=10, y=10, environment=env, color="blue")
    env.add_agent(agent)
    env.add_agent(agent2)

    viz = Visualization(root, env)

    def update():
        env.step()
        viz.draw()
        root.after(100, update)
    
    update()
    root.mainloop()

if __name__ == "__main__":
    # Set up signal handler before calling main()
    signal.signal(signal.SIGINT, shutdown_simulation)
    main()
