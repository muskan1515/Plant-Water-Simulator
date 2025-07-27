# weather.py
import requests

def get_current_location():
    try:
        r = requests.get("https://ipinfo.io/json")
        data = r.json()
        print(r,data)
        return data["city"]
    except Exception as e:
        return None

def get_weather(city, api_key):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        r = requests.get(url)
        data = r.json()
        weather_main = data["weather"][0]["main"].lower()
        print(city, api_key, url, r, data, weather_main)
        return {
            "temperature": data["main"]["temp"],
            "rain": "rain" in weather_main,
            "weather": data["weather"][0]["main"]
        }
    except Exception as e:
        return {
            "temperature": 25,
            "rain": False,
            "weather": "Clear"
        }
