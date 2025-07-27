# garden.py
from plant import Plant, Cactus, Fern

class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_type, name):
        if plant_type.lower() == 'cactus':
            plant = Cactus(name)
        elif plant_type.lower() == 'fern':
            plant = Fern(name)
        else:
            plant = Plant(name)
        print(self.plants)
        self.plants.append(plant)

    def water_all(self, agent=None):
        for plant in self.plants:
            if not agent or agent.should_water():
                plant.water(source='AI' if agent else 'manual')

    def get_all(self):
        return self.plants
