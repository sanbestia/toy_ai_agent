# toy_ai_agent

A hands-on course project from the [boot.dev](https://boot.dev) curriculum exploring how AI agents actually work. It's a working implementation of an agentic loop — Gemini receives a prompt, decides which tools to call, acts on them, and reasons about the results until the task is done.

It's intentionally minimal. The goal was to understand the mechanics, not to build something production-ready.

> ⚠️ **Heads up:** the agent can read, write, and execute Python files on your machine with no real guardrails. Fine for experimenting locally, not something you'd want to deploy.

---

## How it works

1. You give it a prompt from the command line
2. It calls the Gemini API with a system prompt and a set of available tools
3. It executes whatever tool calls the model requests (file reads, writes, running scripts)
4. It feeds the results back and repeats until the task is complete or it hits the loop limit (`MAX_LOOPS` modifiable in `config.py`)

---

## Project Structure

```
toy_ai_agent/
├── main.py                            # Entry point — runs the agent loop
├── config.py                          # Model name, loop limit, max chars
├── prompts.py                         # System prompt
└── functions/
    ├── call_function.py               # Dispatches tool calls
    ├── get_function_call_by_model.py  # Parses Gemini's tool-use response
    ├── get_files_info.py              # Lists files in the working directory
    ├── get_file_content.py            # Reads a file's contents
    ├── get_abs_path_in_wd.py          # Path resolution helper
    ├── write_file.py                  # Writes to a file
    └── run_python_file.py             # Executes a Python script
```

---

## Running it

You'll need Python 3.13+ and [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync
```

Add a `.env` with your [Gemini API key](https://aistudio.google.com/):

```env
GEMINI_API_KEY='your-key-here'
```

Then run:

```bash
uv run python main.py "your prompt here"
```

---

## What I learned building this

- How an agentic loop actually works at the code level: prompt → model → tool call → result → repeat
- How LLMs handle tool/function calling at the API level
- Why real-world agents need careful sandboxing — implementing even a basic version makes the challenges immediately concrete

---

*Built as part of the [boot.dev](https://boot.dev) backend curriculum.*
