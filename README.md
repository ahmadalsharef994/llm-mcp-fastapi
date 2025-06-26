# MCP + FastAPI + Ollama 🧠🚀

This repo is a minimal backend for exposing tools to local LLMs (like LLaMA 3 via Ollama) using the [Model Context Protocol (MCP)](https://modelcontextprotocol.org).

## 🛠 Features

- [x] FastAPI backend
- [x] Tool listing (`/mcp/tools/list`)
- [x] Tool invocation (`/mcp/tools/invoke`)
- [x] Example: `get_weather(city)`
- [x] Works with Ollama and any LLM that supports tool calling

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/llm-mcp-fastapi.git
cd llm-mcp-fastapi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Installation
1. Install Python 3.x and FastAPI.
2. Install Ollama CLI and download required models (e.g., `ollama pull mistral`).
3. Clone the repository: `git clone https://github.com/ahmadalsharef994/llm-mcp-fastapi.git`
4. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Start the server: `uvicorn main:app --reload`
2. Send a chat request: `curl -X POST "http://localhost:8000/chat" -d '{"message": "Hello"}'`

## Project Structure
- `main.py`: FastAPI application
- `ollama_config/`: Ollama integration settings

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
