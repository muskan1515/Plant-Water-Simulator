#plant.py

from datetime import datetime

class Plant:
    def __init__(self, name, water_need = 1):
        self.name = name
        self.water_level = 1
        self.water_need = water_need
        self.history = []
        self.growth = 0
    
    def water(self, source='manual'):
        self.water_level += 1
        self.growth += 1
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "source": source,
        })

    def needs_water(self):
        return self.water_level < self.water_need

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}, Level={self.water_level}, Growth={self.growth}>"
    


class Cactus(Plant):
    def __init__(self, name):
        super(Cactus, self).__init__(name, water_need = 1)


class Fern(Plant):
    def __init__(self, name):
        super(Fern, self).__init__(name, water_need = 3)