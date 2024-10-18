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

    def set_obj_coordinates(self, obj, x, y, z):
        new_coords = (x, y, z)
        old_coords = self.get_obj_coordinates(obj)

        # If the object is already at the specified coordinates, do nothing
        if old_coords == new_coords:
            logger.debug(f"{obj.__class__.__name__ if obj else 'Object'} is already at {new_coords}")
            return

        # Check if another object is already at the new coordinates
        existing_obj = self.inspect_coordinate(*new_coords)
        if existing_obj:
            logger.warning(f"Another object ({existing_obj.__class__.__name__}) is already at {new_coords}")
            return
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

    def get_obj_coordinates(self, obj):
        logger.info(f"Getting location of {obj.__class__.__name__}")
        for key, value in self.grid.items():
            if value == obj:
                logger.debug(f"Found {obj.__class__.__name__} at {key}")
                return key
        return None
    
    def inspect_coordinate(self, x, y, z):
        logger.info(f"Inspecting grid location {x}, {y}, {z}")
        return self.grid.get((x, y, z), None)
    

# Titans

class Titan:
    def __init__(self, grid):
        self.grid = grid

    def move(self, x=1, y=1, z=0):
        "get location and move to new location by a random amount"

        coordinates = self.grid.get_obj_coordinates(self)

        if coordinates:
            x, y, z = coordinates
            x += random.randint(-2, 2)
            y += random.randint(-2, 2)
            self.grid.set_obj_coordinates(self, x, y, z)
            logger.info(f"{self.__class__.__name__} moved to {x}, {y}, {z}")

class Scorch(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000


class Ronin(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000


class Northstar(Titan):
    def __init__(self, grid):
        super().__init__(grid)
        self.health = 1000
            

def run():

    grid = Grid()
    scorch = Scorch(grid)
    grid.set_obj_coordinates(scorch, 10, 10, 0)
    logger.info(f"{scorch.__class__.__name__} is on the grid: {scorch.grid.get_obj_coordinates(scorch)}")

    ronin = Ronin(grid)
    grid.set_obj_coordinates(ronin, 10, 11, 0)
    logger.info(f"{ronin.__class__.__name__} is on the grid: {ronin.grid.get_obj_coordinates(ronin)}")

    northstar = Northstar(grid)
    grid.set_obj_coordinates(northstar, 10, 9, 0)
    logger.info(f"{northstar.__class__.__name__} is on the grid: {northstar.grid.get_obj_coordinates(northstar)}")


    while True:
        scorch.move()
        ronin.move()
        northstar.move()
        time.sleep(1)
 
if __name__ == "__main__":
    run()
