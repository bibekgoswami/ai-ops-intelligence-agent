from crewai import Agent

ops_agent = Agent(
    role="AI Operations Analyst",
    goal="Analyze operational events and recommend corrective actions",
    backstory=(
        "You are a senior operations engineer who specializes in identifying "
        "production risks, failures, and inefficiencies from system events."
    ),
    verbose=True
)
