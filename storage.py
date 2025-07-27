# storage.py
import json
from plant import Plant, Cactus, Fern

def save_garden(garden, path="garden.json"):
    with open(path, "w", newline='') as f:
        json.dump([{**vars(p), "__class__": p.__class__.__name__} for p in garden.plants], f)

def load_garden(path="garden.json"):
    from garden import Garden
    try:
        with open(path, "r") as f:
            data = json.load(f)
        g = Garden()
        for p in data:
            cls = {"Plant": Plant, "Cactus": Cactus, "Fern": Fern}.get(p.get("__class__", "Plant"), Plant)
            plant = cls(p["name"])
            plant.water_level = p["water_level"]
            plant.growth = p["growth"]
            plant.history = p["history"]
            g.plants.append(plant)
        return g
    except:
        return Garden()
