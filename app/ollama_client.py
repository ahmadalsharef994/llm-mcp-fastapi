import httpx

OLLAMA_OPENAI_URL = "http://localhost:11434/v1/chat/completions"

async def query_ollama(prompt: str, model: str = "llama3.2:1b"):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(OLLAMA_OPENAI_URL, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
