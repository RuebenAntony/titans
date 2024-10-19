"""
# Titans AI

Titans is a turn based strategy game where two teams of titans battle each other. By Rueben Antony

Features to implement:

- Grid based movement
- Turn based
- Different classes of titans with unique abilities, health, and movement
- Titan classes will also have strategic role types: tank, support, flanker
- Different types of terrain with different movement costs
- Different types of terrain with different attack/defense bonuses
- Different types of terrain with different vision ranges
- Fog of war

## AI team and character control via inference using LLMs

AI feature ideas to implement:

- Each team will have a leader pilot that will instruct the titans
- Titans in the same team will be able to communicate with each other during battle
- Titans will update each other on the status of the titans and the battle

## Human voice or text-based control

- The human player will be able to control the titans via voice or text commands
- or, the human can control via CLI commands

## Other notes & ideas

NEED CLASS TEAM A TEAM WILL HAVE THREE TYPES OF TITANS TANK, SUPPORT AND FLANKER

THEY WILL ALL HAVE DIFFERENT ABILITIES AND DIFFERENT HEALTH AND MOVEMENT
AND THEY WILL HAVE TO BE ABLE TO WORK TOGETHER AS A TEAM USING THOSE ABILITIES STRATEGICALLY
TO GAIN CONTROL OF THE HARVESTER ON GRID LOCATION 0,0 IN THE CENTER OF THE MAP ONCE IN POSSESSION THE HARVESTER NEEDS TO BE PROTECTED FROM OTHER TITANS
FOR ? AMOUNT OF TURNS AFTER WHICH THE TEAM IN CONTROL OF THE HARVESTER WILL BE DECLARED THE WINNER

CLASS IDEAS:SCORCH FIRE BASED TANK,RONIN ELECTRIC SWORD FLANKER,NORTHSTAR HOVER SNIPER SUPPORT,MORE TITANS TO COME?
EACH TURN THE PLAYER WILL SELECT A TURN ACTION FOR EACH TITAN
THE TURN ACTIONS ARE MOVE, ATTACK, AND ABILITY
MOVE ALLOWS THE TITAN TO MOVE TO AN AMOUNT OF SQUARES BASED ON THEIR MOVEMENT/CLASS
ATTACK ALLOWS THE TITAN TO ATTACK ANOTHER TITAN DEALING DAMAGE (THE RANGE WILL VARY BASED ON THE TITAN)
ABILITIES WILL VARY BY TITAN BUT WILL HAVE A COOLDOWN AFTER THEY USE IT
IF TITAN IS KILLED IT WILL BE REMOVED FROM THE GRID AND THE GAME WILL CONTINUE MAYBE IT CAN BE RESPAWNED?
IF IT CAN BE RESPAWNED THEN WE SHOULD HAVE A CONDITION THAT NEEDS TO BE MET BEFORE A NEW TITAN CAN BE RESPAWNED

Pre-set strategies.  The human player can select a pre-set strategy before the game starts and the AI will use that strategy.

Tasks:
- create a grid, have a single titan move around on it, with testing and logging

"""


import time
import random

from logger.logger_config import get_logger

logger = get_logger(__name__)

# Grid

class Grid:
    "Grid is a 3D infinite voxel space"

    def __init__(self):
        self.grid = {}

    def set_obj_coordinates(self, obj, x, y, z=0):
        new_coords = (x, y, z)
        old_coords = self.get_obj_coordinates(obj)

        # If the object is already at the specified coordinates, do nothing
        if old_coords == new_coords:
            logger.debug(f"{obj.__class__.__name__ if obj else 'Object'} is already at {new_coords}")
            return

        # Check if another object is already at the new coordinates
        existing_obj = self.inspect_coordinate(*new_coords)
        if existing_obj:
            logger.warning(f"Another ({existing_obj.__class__.__name__}) is already at {new_coords}")
            return False
        logger.info(f"Setting value at {new_coords} to {obj.__class__.__name__ if obj else 'None'}")

        # Remove the object from its previous location if it exists
        if old_coords:
            self.grid.pop(old_coords)
            logger.info(f"Removed {obj.__class__.__name__} from old location {old_coords}")

        if obj is None:
            self.grid.pop(new_coords, None)
            logger.info(f"Grid location {new_coords} is now empty")
        else:
            self.grid[new_coords] = obj
            logger.info(f"Grid location {new_coords} is now {obj.__class__.__name__}")

        return new_coords

    def get_obj_coordinates(self, obj):
        logger.info(f"Getting location of {obj.__class__.__name__}")
        for key, value in self.grid.items():
            if value == obj:
                logger.debug(f"Found {obj.__class__.__name__} at {key}")
                return key
        return None
    
    def inspect_coordinate(self, x, y, z):
        return self.grid.get((x, y, z), None)
    
class Team:
    def __init__(self, name):
        self.name = name
        self.titans = []
        logger.info(f"Team {self.name} created")

    def add_titan(self, titan):
        self.titans.append(titan)
        logger.info(f"{titan.__class__.__name__} added to team {self.name}")








# Titans

class Titan:

    def __init__(self, grid):
        self.grid = grid

    def titan_fall(self, x, y, z=0):
        self.grid.set_obj_coordinates(self, x, y, z)

    def scan(self):
        current_coordinates = self.grid.get_obj_coordinates(self)
        if not current_coordinates:
            logger.error(f"{self.__class__.__name__} is not on the grid.")
            return []

        x, y, z = current_coordinates
        scanned_objects = []

        for dx in range(-self.scan_range, self.scan_range + 1):
            for dy in range(-self.scan_range, self.scan_range + 1):
                for dz in range(-self.scan_range, self.scan_range + 1):
                    scan_x, scan_y, scan_z = x + dx, y + dy, z + dz
                    if scan_x == x and scan_y == y and scan_z == z:
                        continue  # Skip the titan's own position
                    obj = self.grid.inspect_coordinate(scan_x, scan_y, scan_z)
                    if obj is not None and obj != self:
                        logger.info(f"Scanned {obj.__class__.__name__} at {scan_x}, {scan_y}, {scan_z}")
                        scanned_objects.append((obj, (scan_x, scan_y, scan_z)))

        logger.info(f"{self.__class__.__name__} scanned {len(scanned_objects)} objects within range {self.scan_range}")
        return scanned_objects

    def move(self, delta_x=0, delta_y=0, delta_z=0):

        current_coordinates = self.grid.get_obj_coordinates(self)
        if not current_coordinates:
            logger.error(f"{self.__class__.__name__} is not on the grid.")
            return

        new_coordinates = (
            current_coordinates[0] + delta_x,
            current_coordinates[1] + delta_y,
            current_coordinates[2] + delta_z
        )

        # Check if the move is within the move_range
        if abs(delta_x) <= self.move_range and abs(delta_y) <= self.move_range and abs(delta_z) <= self.move_range:

            occupant = self.grid.inspect_coordinate(*new_coordinates)
            if occupant is not None:
                logger.warning(f"Move to {new_coordinates} blocked by {occupant.__class__.__name__}")
                return current_coordinates
            
            self.grid.set_obj_coordinates(self, *new_coordinates)
            logger.info(f"{self.__class__.__name__} moved to {new_coordinates}")
            return new_coordinates
        else:
            logger.warning(f"Move by {delta_x, delta_y, delta_z} is out of range for {self.__class__.__name__}")
            return current_coordinates
        
        
class Scorch(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000
        self.move_range = 5
        self.scan_range = 15

class Ronin(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000
        self.move_range = 10
        self.scan_range = 15

class Northstar(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000
        self.move_range = 7
        self.scan_range = 15

def run():
    red_team = Team("Red")
    blue_team = Team("Blue")

    grid = Grid()
    scorch_red = Scorch(grid)
    scorch_red.titan_fall(10, 10, 0)
    logger.info(f"{scorch_red.__class__.__name__} is on the grid: {scorch_red.grid.get_obj_coordinates(scorch_red)}")
    red_team.add_titan(scorch_red)

    ronin_red = Ronin(grid)
    ronin_red.titan_fall(10, 11, 0)
    logger.info(f"{ronin_red.__class__.__name__} is on the grid: {ronin_red.grid.get_obj_coordinates(ronin_red)}")
    red_team.add_titan(ronin_red)

    northstar_red = Northstar(grid)
    northstar_red.titan_fall(10, 9, 0)
    logger.info(f"{northstar_red.__class__.__name__} is on the grid: {northstar_red.grid.get_obj_coordinates(northstar_red)}")
    red_team.add_titan(northstar_red)

    scorch_blue = Scorch(grid)
    scorch_blue.titan_fall(10, 10, 0)
    logger.info(f"{scorch_blue.__class__.__name__} is on the grid: {scorch_blue.grid.get_obj_coordinates(scorch_blue)}")
    blue_team.add_titan(scorch_blue)

    ronin_blue = Ronin(grid)
    ronin_blue.titan_fall(10, 11, 0)
    logger.info(f"{ronin_blue.__class__.__name__} is on the grid: {ronin_blue.grid.get_obj_coordinates(ronin_blue)}")
    blue_team.add_titan(ronin_blue)

    northstar_blue = Northstar(grid)
    northstar_blue.titan_fall(10, 9, 0)
    logger.info(f"{northstar_blue.__class__.__name__} is on the grid: {northstar_blue.grid.get_obj_coordinates(northstar_blue)}")
    blue_team.add_titan(northstar_blue)

    while True:
        scorch.move(
            delta_x=random.randint(-scorch.move_range, scorch.move_range), 
            delta_y=random.randint(-scorch.move_range, scorch.move_range)
        )
        ronin.move(
            delta_x=random.randint(-ronin.move_range, ronin.move_range), 
            delta_y=random.randint(-ronin.move_range, ronin.move_range)
        )
        northstar.move(
            delta_x=random.randint(-northstar.move_range, northstar.move_range), 
            delta_y=random.randint(-northstar.move_range, northstar.move_range)
        )
        time.sleep(1)
 
if __name__ == "__main__":
    run()
