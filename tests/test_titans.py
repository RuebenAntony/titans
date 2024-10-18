from titans.game import Titan, Scorch

def test_titan_initialization():
    titan = Titan()
    assert titan.health == 1000, "Titan's health should be 1000 by default."

def test_scorch_initialization():
    scorch = Scorch()
    assert scorch.health == 1000, "Scorch should inherit health from Titan."
    assert scorch.type == "Scorch", "Scorch's type should be set to 'Scorch'."