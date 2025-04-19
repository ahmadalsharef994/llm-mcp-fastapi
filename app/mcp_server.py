from fastapi import APIRouter, Request
from app.tools.weather import get_weather, WeatherInput

mcp_router = APIRouter()

@mcp_router.post("/tools/list")
async def list_tools():
    return {
        "tools": [
            {
                "name": "get_weather",
                "description": "Get the current weather for a city.",
                "parameters": WeatherInput.schema()
            }
        ]
    }

@mcp_router.post("/tools/invoke")
async def invoke_tool(request: Request):
    body = await request.json()
    tool_name = body.get("tool_name")
    arguments = body.get("arguments", {})

    if tool_name == "get_weather":
        input_data = WeatherInput(**arguments)
        result = get_weather(input_data)
        return {"result": result}
    else:
        return {"error": f"Tool '{tool_name}' not found."}
