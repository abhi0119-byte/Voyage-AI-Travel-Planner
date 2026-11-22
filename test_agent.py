
from agents.destination_agent import DestinationAgent

agent = DestinationAgent()

result = agent.recommend("Manali")

print("Recommended Places:")

for place in result:
    print("-", place)
