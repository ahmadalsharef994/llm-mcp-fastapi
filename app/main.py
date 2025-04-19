from fastapi import FastAPI
from app.ollama_client import query_ollama
from app.mcp_server import mcp_router  # if you're still using this

app = FastAPI()

# Optional: include MCP router
app.include_router(mcp_router, prefix="/mcp")

@app.get("/ask")
async def ask(prompt: str):
    reply = await query_ollama(prompt)
    return {"response": reply}
