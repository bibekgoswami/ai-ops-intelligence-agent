from crewai import Task

def analyze_event_task(agent, event_data):
    return Task(
        description=f"""
        Analyze the following operational event:

        {event_data}

        Identify:
        1. What is going wrong
        2. Risk severity (LOW / MEDIUM / HIGH)
        3. Possible root causes
        4. Recommended next actions
        """,
                agent=agent,
                expected_output="""
        Structured analysis with:
        - Issue summary
        - Severity
        - Root cause hypothesis
        - Actionable recommendations
        """
    )
