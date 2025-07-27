# 🌿 Smart Plant Watering Simulation (Python 2.7)

This is an **AI-assisted CLI plant watering system** built in **Python**, that simulates different types of plants with unique watering needs. It uses **real weather data** via OpenWeatherMap API, applies **OOP principles**, persists garden state using JSON, and includes a basic **smart watering agent** that learns how and when to water your plants.

---

## 🚀 Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🌱 **Multiple Plant Types**       | Add `Cactus`, `Fern`, or other plant types with different watering needs.  |
| 🧬 **Inheritance-based OOP**      | Each plant is a subclass of a `Plant` base class.                          |
| 🧠 **Smart AI Watering Agent**    | Automatically decides whether to water based on time, type, and weather.  |
| 🌦️ **Live Weather via API**       | Uses OpenWeatherMap API to check local weather conditions.                |
| 💾 **Persistent Storage**         | Saves and loads full garden state to/from a JSON file.                    |
| 🔧 **Simulation Actions**         | Add plant, water manually, check status of all plants.                    |
| 📊 **Daily Plant Simulation**     | Updates water level, health, and status of each plant every run.         |

---

## 🏗️ Project Structure

```bash
plant_simulation/
├── main.py              # Main CLI logic
├── cli.py              # To have all the cli script to handle all the commands flow
├── plant.py             # Base Plant class + subclasses (Cactus, Fern)
├── garden.py            # Garden class to manage plants
├── weather.py           # Real-time weather using OpenWeatherMap API
├── ai_agent.py             # SmartWateringAgent for intelligent watering
├── plotter.py           # Line Plot to show all plants growth to time scenario
├── garden.json          # Auto-generated JSON file (plant states)
├── simulate.py          #Simulation script that works for all the available plants 
├── requirement.txt      #showing all the requirement modules for this
├── command.txt          #have all the default commands to run this simulation
├── config.py            # Contains API keys (ignored in .gitignore)
└── README.md            # This file
