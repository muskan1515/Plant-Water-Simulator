# test_weather.py
from weather import get_current_location, get_weather
from config import OPENWEATHER_API_KEY

def test_weather_fetch():
    city = get_current_location()
    assert city is not None

    api_key = OPENWEATHER_API_KEY  
    weather_data = get_weather(city, api_key)

    assert "temperature" in weather_data
    assert "rain" in weather_data
    assert "weather" in weather_data
    print("Weather Data:", weather_data)
