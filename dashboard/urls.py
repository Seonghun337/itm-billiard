from django.urls import path
from . import views
# from .views import GameList


urlpatterns = [
    path('create_game/',views.create_game),
    path('', views.GameList.as_view()),
]