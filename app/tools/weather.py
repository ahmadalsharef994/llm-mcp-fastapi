from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str

def get_weather(input: WeatherInput) -> str:
    # Placeholder implementation
    return f"The weather in {input.city} is sunny with 25°C."
