import tkinter as tk

class Visualization:
    def __init__(self, root, environment):
        self.root = root
        self.env = environment
        self.canvas = tk.Canvas(self.root, width=400, height=400, )
        self.canvas.pack()
        self.draw
    
    def draw(self):
        self.canvas.delete("all")
        self.draw_grid()
        for agent in self.env.agents:
            self.draw_agent(agent)

    def draw_grid(self):
        separation = 10
        for i in range(0, 400, separation):
            self.canvas.create_line(i, 0, i, 400)
            self.canvas.create_line(0, i, 400, i)

    def draw_agent(self, agent):
        size = 10
        x1, y1 = agent.x * size, agent.y * size
        x2, y2 = x1 + size, y1 + size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=agent.color)