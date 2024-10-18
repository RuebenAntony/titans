from titans.game import Titan, Scorch, Ronin, Northstar, Grid

grid = Grid()

def test_grid_initialization():
    assert grid.grid == {}, "Grid should be empty."

def test_titan_initialization():
    titan = Titan(grid)
   

def test_scorch_initialization():
    # grid = Grid()
    scorch = Scorch(grid)
    assert scorch.health == 1000, "Scorch should inherit health from Titan."
    
def test_ronin_initialization():
    # grid = Grid()
    ronin = Ronin(grid)
    assert ronin.health == 1000, "Ronin should inherit health from Titan."

def test_northstar_initialization():
    # grid = Grid()
    northstar = Northstar(grid)
    assert northstar.health == 1000, "Northstar should inherit health from Titan."

def test_scorch_move():
    scorch = Scorch(grid)
    grid.set_obj_coordinates(scorch, 0, 0)
    assert scorch.move(delta_x=1, delta_y=1) == (1, 1, 0), "Scorch should move to (1, 1, 0)."

def test_ronin_move():
    ronin = Ronin(grid)
    grid.set_obj_coordinates(ronin, 0, 0)
    assert ronin.move(delta_x=2, delta_y=2) == (2, 2, 0), "Ronin should move to (2, 2, 0)."

def test_northstar_move():
    northstar = Northstar(grid)
    grid.set_obj_coordinates(northstar, 0, 0)
    assert northstar.move(delta_x=3, delta_y=3) == (3, 3, 0), "Northstar should move to (3, 3, 0)."

def test_scorch_collision():
    grid = Grid()
    scorch = Scorch(grid)
    ronin = Ronin(grid)
    
    # Place Scorch at (0, 0, 0)
    grid.set_obj_coordinates(scorch, 0, 0, 0)
    
    # Place Ronin at (1, 1, 0)
    grid.set_obj_coordinates(ronin, 1, 1, 0)
    
    # Attempt to move Scorch to Ronin's position
    new_position = scorch.move(delta_x=1, delta_y=1)
    
    # Assert that Scorch didn't move
    assert new_position == (0, 0, 0), "Scorch should not move into Ronin's position"
    
    # Verify that Ronin is still at its original position
    assert grid.get_obj_coordinates(ronin) == (1, 1, 0), "Ronin should remain at its original position"
    
    # Verify that Scorch is still at its original position
    assert grid.get_obj_coordinates(scorch) == (0, 0, 0), "Scorch should remain at its original position"
