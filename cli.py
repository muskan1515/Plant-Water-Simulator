# cli.py
import argparse
from storage import save_garden, load_garden
from ai_agent import SmartWateringAgent
from plotter import plot_water_growth
from simulate import simulate_watering_all
from config import OPENWEATHER_API_KEY

def cli_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", nargs=2, help="Add plant: <type> <name>")
    parser.add_argument("--water", action="store_true", help="Water all plants")
    parser.add_argument("--agent", action="store_true", help="Use AI watering agent")
    parser.add_argument("--plot", action="store_true", help="Plot watering/growth")
    parser.add_argument("--simulate", nargs="?", const=True , default=False, help="Simulate full watering scenario")
    args = parser.parse_args()

    if args.simulate:
        simulate_watering_all()
        return

    garden = load_garden()

    if args.add:
        garden.add_plant(args.add[0], args.add[1])

    if args.water:
        agent = SmartWateringAgent(OPENWEATHER_API_KEY) if args.agent else None
        garden.water_all(agent)

    save_garden(garden)

    for p in garden.get_all():
        print(p)

    if args.plot:
        plot_water_growth(garden)
