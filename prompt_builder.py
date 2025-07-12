## TO-DO integrate with some type of AI tool 
def build_prompt(log: str, trace: str) -> str:
    return f"""
You are a backend debugging assistant. Analyze the following logs and stack trace. Identify the root cause and suggest a fix.

LOG:
{log}

STACK TRACE:
{trace}
"""
