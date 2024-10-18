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

from logger.logger_config import get_logger

logger = get_logger(__name__)


# Titans

class Titan:
    def __init__(self):
        self.health = 1000


class Scorch(Titan):
    def __init__(self):
        super().__init__()
        self.type = "Scorch"

def run():
    while True:
        scorch = Scorch()
        logger.info(scorch.health)

        time.sleep(1)
        logger.warning(scorch.type)

        time.sleep(1)
        logger.error("This is an error MESSAGE")

        time.sleep(1)
        logger.critical("This is a critical message")

        time.sleep(1)
        logger.debug("This is a debug message")

        time.sleep(1)

if __name__ == "__main__":
    run()