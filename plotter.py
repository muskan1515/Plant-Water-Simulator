# plotter.py
import matplotlib.pyplot as plt
from datetime import datetime

def plot_water_growth(garden):
    for plant in garden.get_all():
        times = [datetime.fromisoformat(e["timestamp"]) for e in plant.history]
        growth = list(range(1, len(times) + 1))
        sources = [e["source"] for e in plant.history]

        plt.plot(times, growth, label=plant.name)
        for i, s in enumerate(sources):
            if s == 'AI':
                plt.scatter(times[i], growth[i], color='green', marker='x', label="AI" if i == 0 else "")
            else:
                plt.scatter(times[i], growth[i], color='blue', marker='o', label="Manual" if i == 0 else "")

    plt.xlabel("Time")
    plt.ylabel("Growth Level")
    plt.title("Plant Growth Tracker")
    plt.legend()
    plt.show()
