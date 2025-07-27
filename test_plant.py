# test_plant.py
from plant import Plant

def test_water():
    p = Plant("Test")
    p.water()
    assert p.water_level == 2
    assert p.growth == 1
    assert len(p.history) == 1

def test_needs_water():
    p = Plant("Test", water_need=2)
    assert p.needs_water()
    p.water()
    p.water()
    assert not p.needs_water()
