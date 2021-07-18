from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    played_at = models.DateTimeField()
    winners = models.ManyToManyField(User, blank=True, related_name='win')
    losers = models.ManyToManyField(User, blank=True, related_name='lose')
    num_players = models.IntegerField()

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()