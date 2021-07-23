from django.db import models
from django.contrib.auth.models import User
# from datetime import date
from django.utils import timezone


class Game(models.Model):
    played_at = models.DateTimeField(auto_now_add=True)
    num_players = models.IntegerField()


# Create your models here.
class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    win = models.BooleanField()

    class Meta:
        ordering=['win','player']