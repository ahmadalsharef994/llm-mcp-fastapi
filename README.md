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
