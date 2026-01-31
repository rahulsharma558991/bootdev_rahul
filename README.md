# Toy Claude Code - AI Coding Agent

A toy implementation of Claude Code (Cursor/Zed's Agentic Mode) using Google's Gemini API. This project demonstrates how to build an AI agent that can read files, write files, list directories, and execute Python code.

## ⚠️ Important Disclaimer

**This is a TOY/EDUCATIONAL VERSION ONLY.** What we've built here is a simplified version of something like Cursor/Zed's Agentic Mode or Claude Code. Even their tools aren't perfectly secure, so be careful what you give them access to. 

**DO NOT use this toy agent as-is in production or with untrusted prompts!** There are significant security concerns:
- The agent has broad file system access
- It can execute arbitrary Python code
- There are minimal sandbox protections
- Path traversal attacks are possible if not carefully validated

Use this only for educational purposes and development in isolated, controlled environments.

## Features

- **List Files**: Use `get_files_info()` to explore directory structures
- **Read Files**: Use `get_file_content()` to read file contents
- **Write Files**: Use `write_file()` to create or modify files
- **Execute Python**: Use `run_python_file()` to run Python scripts

## Prerequisites

- Python 3.12 or higher
- A Google Gemini API key
- `uv` package manager (or pip)

## Setup Instructions

### 1. Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Create Environment File

In the `toy-claude-code/` directory, create a `.env` file:

```bash
cd toy-claude-code
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

Replace `your_actual_api_key_here` with your actual Gemini API key.

### 3. Install Dependencies

Using `uv`:
```bash
uv sync
```

Or using pip:
```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

## Usage

### Basic Usage

Run the agent with a prompt:

```bash
uv run main.py "your question or task here"
```

### Example Commands

Ask the agent to explore a calculator project:
```bash
uv run main.py "how does the calculator render results to the console?"
```

List files in a directory:
```bash
uv run main.py "list all files in the calculator directory"
```

Execute a test file:
```bash
uv run main.py "run the calculator tests and tell me the results"
```

### Verbose Mode

Enable verbose output to see token usage:

```bash
uv run main.py "your question" --verbose
```

## Project Structure

```
toy-claude-code/
├── main.py                 # Entry point and main logic
├── config.py              # Configuration (MAX_CHARS, etc.)
├── pyproject.toml         # Project dependencies
├── .env                   # API key (create this file)
├── functions/
│   ├── call_function.py   # Function dispatcher
│   ├── get_files_info.py  # List files implementation
│   ├── get_file_content.py # Read files implementation
│   ├── write_file.py      # Write files implementation
│   ├── run_python_file.py # Execute Python files
│   └── prompts.py         # System prompts for the AI
└── calculator/            # Example project for testing
    ├── main.py
    ├── tests.py
    └── pkg/
```

## How It Works

1. User provides a prompt to the agent
2. The agent processes the prompt with Google Gemini API
3. If Gemini decides function calls are needed, the agent:
   - Calls the appropriate function (`get_files_info`, `get_file_content`, `write_file`, or `run_python_file`)
   - Returns the result back to Gemini
   - Gemini decides next steps based on the result
4. This loop repeats until the agent provides a final response

## Configuration

Edit `config.py` to adjust settings:

```python
MAX_CHARS = 10000        # Maximum characters to read from a file
MAX_ITERS = 20           # Maximum iterations before giving up
```

## Testing

The project includes test files for individual functions:

```bash
uv run test_get_file_content.py
uv run test_get_files_info.py
uv run test_write_file.py
uv run test_run_python_file.py
```

## Security Considerations

While this toy version includes some basic path validation:
- It restricts operations to the working directory
- It prevents directory traversal with `os.path.commonpath()` checks

This is NOT sufficient for production use. Before deploying any agent-based code execution system, consider:
- Running in sandboxed environments (containers, VMs)
- Implementing strict allowlists of permitted operations
- Adding comprehensive audit logging
- Using capability-based security models
- Regular security audits

## Educational Value

This project is useful for learning:
- How AI agents can interact with file systems
- Building tool-use interfaces with LLMs
- The Google Gemini API and function calling
- Prompt engineering for code-related tasks
- The basics of agent loop architecture

## License

Educational use only. See disclaimer above.
