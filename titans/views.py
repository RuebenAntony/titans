from django.shortcuts import render

def index(request):
    """
    Main view for the Titans game. Renders the game interface and handles game state.
    """
    context = {
        'title': 'Titans - Strategic Battle Game',
        'author': 'Rueben Antony',
    }
    return render(request, 'index.html', context)
