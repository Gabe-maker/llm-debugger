# debugger

**A simple CLI tool that processes backend logs and stack traces, generating a formatted prompt to feed into ChatGPT or other LLMs for debugging assistance.**

---

## Features

- Accepts log input via **file argument** or **stdin pipe**  
- Cleans and truncates logs for readability  
- Extracts stack traces from logs (Python, Java-style)  
- Generates a natural-language prompt you can copy-paste into ChatGPT  
- Helps accelerate root cause analysis and fix suggestions without needing API keys or paid plans  

---

## Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/debugger.git
   cd debugger
   ```

2. (Optional) Create a Python virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt 
    playright install
    ```
3. Make the CLI script executable:
    ```bash
        chmod +x debugger.py
    ```
4. (Optional) Add debugger to your PATH for global use:

    ```bash
        ln -s $(pwd)/debugger.py /usr/local/bin/debugger
    ```

5. Usage
You can provide logs either by piping them or passing a file path:

```
# Pipe a log file
cat path/to/error.log | debugger

# Or pass the log file as an argument
debugger path/to/error.log

```
