from titans.game import Titan, Scorch, Ronin, Northstar, Grid

global_grid = Grid()

def test_grid_initialization():
    assert global_grid.grid == {}, "Grid should be empty."

def test_titan_initialization():
    titan = Titan(global_grid)
   
def test_scorch_initialization():
    scorch = Scorch(global_grid)
    assert scorch.health == 1000, "Scorch should inherit health from Titan."
    
def test_ronin_initialization():
    ronin = Ronin(global_grid)
    assert ronin.health == 1000, "Ronin should inherit health from Titan."

def test_northstar_initialization():
    northstar = Northstar(global_grid)
    assert northstar.health == 1000, "Northstar should inherit health from Titan."

def test_scorch_move():
    scorch = Scorch(global_grid)
    scorch.titan_fall(0, 0, 0)
    assert scorch.move(delta_x=1, delta_y=1) == (1, 1, 0), "Scorch should move to (1, 1, 0)."

def test_ronin_move():
    ronin = Ronin(global_grid)
    ronin.titan_fall(0, 0, 0)
    assert ronin.move(delta_x=2, delta_y=2) == (2, 2, 0), "Ronin should move to (2, 2, 0)."

def test_northstar_move():
    northstar = Northstar(global_grid)
    northstar.titan_fall(0, 0, 0)
    assert northstar.move(delta_x=3, delta_y=3) == (3, 3, 0), "Northstar should move to (3, 3, 0)."

def test_scorch_collision():
    collision_grid = Grid()
    scorch = Scorch(collision_grid)
    ronin = Ronin(collision_grid)
    
    # Place Scorch at (0, 0, 0)
    scorch.titan_fall(0, 0, 0)
    
    # Place Ronin at (1, 1, 0)
    ronin.titan_fall(1, 1, 0)
    
    # Attempt to move Scorch to Ronin's position
    new_position = scorch.move(delta_x=1, delta_y=1)
    
    # Assert that Scorch didn't move
    assert new_position == (0, 0, 0), "Scorch should not move into Ronin's position"
    
    # Verify that Ronin is still at its original position
    assert collision_grid.get_obj_coordinates(ronin) == (1, 1, 0), "Ronin should remain at its original position"
    
    # Verify that Scorch is still at its original position
    assert collision_grid.get_obj_coordinates(scorch) == (0, 0, 0), "Scorch should remain at its original position"

def test_scorch_scan():
    scan_grid = Grid()  
    scorch = Scorch(scan_grid)
    ronin = Ronin(scan_grid)
    northstar = Northstar(scan_grid)
    
    scorch.titan_fall(0, 0, 0)
    ronin.titan_fall(1, 1, 0)
    northstar.titan_fall(2, 2, 0)

    scanned_objects = scorch.scan()
    assert len(scanned_objects) == 2, "Scorch should scan 2 objects within range 1."
    assert (ronin, (1, 1, 0)) in scanned_objects, "Ronin should be scanned within range 1."
    assert (northstar, (2, 2, 0)) in scanned_objects, "Northstar should be scanned within range 1."

def test_scorch_titan_fall():
    fall_grid = Grid()
    scorch = Scorch(fall_grid)
    scorch.titan_fall(0, 0, 0)
    assert fall_grid.get_obj_coordinates(scorch) == (0, 0, 0), "Scorch should fall to (0, 0, 0)."

    ronin = Ronin(fall_grid)
    assert not ronin.titan_fall(0, 0, 0), "Ronin should not be able to fall to (0, 0, 0)."
