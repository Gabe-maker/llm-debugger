#!/usr/bin/env python3
import sys
import os
from log_cleaner import clean_log
from stack_parser import extract_stack_trace
from prompt_builder import build_prompt

def main():
    if not sys.stdin.isatty():
        # Read from stdin pipe
        raw_log = sys.stdin.read()
    elif len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        # Read from file argument
        with open(sys.argv[1], 'r') as f:
            raw_log = f.read()
    else:
        print("Usage: debugger [log_file]\nOR pipe log to debugger\nExample: cat error.log | debugger")
        sys.exit(1)

    cleaned_log = clean_log(raw_log)
    stack_trace = extract_stack_trace(cleaned_log)
    prompt = build_prompt(cleaned_log, stack_trace)

    print("\n📋 COPY THIS INTO CHATGPT:\n")
    print(prompt)

if __name__ == "__main__":
    main()
