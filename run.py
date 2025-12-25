import json
from crew import build_crew

with open("inputs/sample_event.json") as f:
    event_data = json.load(f)

crew = build_crew(event_data)
result = crew.kickoff()

print("\n=== AGENT OUTPUT ===\n")
print(result)
