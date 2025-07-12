import re

def clean_log(raw_log: str) -> str:
    # Remove ANSI color codes, truncate long logs, remove noise
    clean = re.sub(r'\x1B[@-_][0-?]*[ -/]*[@-~]', '', raw_log)
    lines = clean.splitlines()

    # Limit to last 100 lines
    trimmed = lines[-100:] if len(lines) > 100 else lines
    return '\n'.join(trimmed)
