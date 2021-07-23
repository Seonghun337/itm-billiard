from django.forms.widgets import ChoiceWidget
from .models import Game,User
from django import forms
from django.forms import widgets


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('num_players',)
