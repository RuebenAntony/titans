import asyncio
import random
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .game import Grid, Scorch, Ronin, Northstar, Team

async def run_game():
    """
    Run the game loop and yield updates asynchronously.
    """
    red_team = Team("Red")
    blue_team = Team("Blue")

    grid = Grid()
    scorch_red = Scorch(grid)
    scorch_red.titan_fall(10, 10, 0)
    red_team.add_titan(scorch_red)

    ronin_red = Ronin(grid)
    ronin_red.titan_fall(10, 11, 0)
    red_team.add_titan(ronin_red)

    northstar_red = Northstar(grid)
    northstar_red.titan_fall(10, 9, 0)
    red_team.add_titan(northstar_red)

    scorch_blue = Scorch(grid)
    scorch_blue.titan_fall(10, 10, 0)
    blue_team.add_titan(scorch_blue)

    ronin_blue = Ronin(grid)
    ronin_blue.titan_fall(10, 11, 0)
    blue_team.add_titan(ronin_blue)

    northstar_blue = Northstar(grid)
    northstar_blue.titan_fall(10, 9, 0)
    blue_team.add_titan(northstar_blue)

    while True:
        scorch_red.move(
            delta_x=random.randint(-scorch_red.move_range, scorch_red.move_range), 
            delta_y=random.randint(-scorch_red.move_range, scorch_red.move_range)
        )
        
        ronin_red.move(
            delta_x=random.randint(-ronin_red.move_range, ronin_red.move_range), 
            delta_y=random.randint(-ronin_red.move_range, ronin_red.move_range)
        )
    
        northstar_red.move(
            delta_x=random.randint(-northstar_red.move_range, northstar_red.move_range), 
            delta_y=random.randint(-northstar_red.move_range, northstar_red.move_range)
        )
        
        # Yield the current state as SSE data
        yield f"data: {scorch_red.grid.get_obj_coordinates(scorch_red)}\n\n"
        
        # Asynchronously sleep to avoid blocking
        await asyncio.sleep(1)

async def game_state(request):
    """
    Asynchronous view to handle Server-Sent Events.
    """
    response = StreamingHttpResponse(
        run_game(),
        content_type='text/event-stream'
    )
    response['Cache-Control'] = 'no-cache'
    return response

def index(request):
    """
    Main view for the Titans game. Renders the game interface.
    """
    context = {
        'title': 'Titans - Strategic Battle Game',
        'author': 'Rueben Antony',
    }
    return render(request, 'index.html', context)
