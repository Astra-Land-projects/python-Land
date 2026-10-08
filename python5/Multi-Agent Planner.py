class Agent:
    def __init__(self, name): self.name = name
    def run(self, task): return f"{self.name} did: {task}"

agents = [Agent("Research"), Agent("Builder"), Agent("Reviewer")]
task = input("Task: ")
for a in agents:
    print(a.run(task))