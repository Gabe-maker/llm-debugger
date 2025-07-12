import re

def extract_stack_trace(log: str) -> str:
    # Simple Python/Java trace matcher
    trace_lines = []
    capture = False

    for line in log.splitlines():
        if "Traceback" in line or re.match(r'\s+at\s', line):
            capture = True
        if capture:
            trace_lines.append(line)
        if capture and line.strip() == "":
            break

    return '\n'.join(trace_lines) if trace_lines else "No stack trace found."
