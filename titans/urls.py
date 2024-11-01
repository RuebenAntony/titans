from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game-state/', views.game_state, name='game_state'),
]
