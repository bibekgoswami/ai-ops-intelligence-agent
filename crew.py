from crewai import Crew
from agent.ops_agent import ops_agent
from task.analyze_event import analyze_event_task

def build_crew(event_data):
    task = analyze_event_task(ops_agent, event_data)
    return Crew(
        agents=[ops_agent],
        tasks=[task],
        verbose=True
    )
