from weather import get_current_location, get_weather
import time
import random
from ai_agent import SmartWateringAgent
from plotter import plot_water_growth
from storage import load_garden
from config import OPENWEATHER_API_KEY

def simulate_watering_all():
    print("🌱 Starting Full Smart Watering Simulation...\n")

    api_key = OPENWEATHER_API_KEY  
    city = get_current_location()
    if not city:
        print("⚠️ Could not detect location. Using default: Delhi")
        city = "Delhi"

    weather = get_weather(city, api_key)

    print("📍 Location: {}".format(city))
    print("🌡️ Temperature: {}°C".format(weather["temperature"]))
    print("🌧️ Weather: {}".format(weather["weather"]))
    print("🌧️ Rain Expected: {}\n".format("Yes" if weather["rain"] else "No"))

    # Load existing garden
    garden = load_garden()
    plants = garden.get_all()

    if not plants:
        print("🚫 No plants found in garden. Add plants first.")
        return

    agent = SmartWateringAgent(api_key)

    for plant in plants:
        print("\n🪴 Simulating for Plant: {}".format(plant.name))

        # Randomize water level (if needed)
        if plant.water_level <= 0:
            plant.water_level = random.randint(1, 5)

        print("💦 Water Level: {}".format(plant.water_level))
        print("📜 History BEFORE watering:")
        for entry in plant.history:
            print(entry)

        time.sleep(1)
        print("\n🤖 AI Agent Evaluating...")

        if agent.should_water(weather):
            print("✅ AI recommends watering. Watering now...")
            plant.water("AI")
        else:
            print("❌ AI does not recommend watering.")

        print("📜 History AFTER watering:")
        for entry in plant.history:
            print(entry)

        print("🌿 Plant Status:\n{}".format(plant))

    print("\n📊 Plotting growth & water history for all plants...")
    plot_water_growth(garden)
