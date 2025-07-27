# ai_agent.py
from weather import get_current_location, get_weather

class SmartWateringAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def should_water(self, weather = None):
        city = get_current_location()
        weather = weather if weather else get_weather(city, self.api_key)
        print(city, weather)
        print(f"📍 City: {city}, Weather: {weather}")
        if weather["rain"]:
            print("🌧️ It's raining. No need to water.")
            return False
        return True
