from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import GameForm
from .models import Game,User,Score
from django.core.exceptions import PermissionDenied, BadRequest
from django.core.paginator import Paginator

import logging
class PlayerList(ListView):
    model = User
    paginate_by = 5

class GameList(ListView):
    model = Game
    ordering = '-played_at'
    paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super(GameList, self).get_context_data()
        context['user_list'] = User.objects.filter(is_staff=False)
        rank_list = self.get_rank_list()
        
        # p = Paginator[rank_list,5]
        context['rank_list'] = rank_list
        context['n_games'] = Game.objects.all().count  
        context['n_rank'] = len(rank_list)
        # context['player_list'] = PlayerList.as_view()
        return context

    def get_rank_list(self):
        rank = list()
        for user in User.objects.filter(is_staff=False).order_by():
            tmp = {}
            tmp['name'] = user.first_name
            nWins = len(Score.objects.filter(player=user,win=True))
            nGames = len(Score.objects.filter(player=user))
            if nGames != 0:
                tmp['win_rate'] = nWins / nGames * 100
            else:
                tmp['win_rate'] = 0.0
            tmp['n_games'] = nGames
            winGames = Score.objects.filter(player=user,win=True)
            avrScore = 0
            if winGames.exists:
                for winGame in winGames:
                    avrScore = avrScore + winGame.score
                    avrScore = avrScore / winGames.count()
            tmp['avr_score'] = avrScore
            if tmp['win_rate'] >= 80:
                tmp['best_user'] = True
            if tmp['win_rate'] <= 20:
                tmp['worst_user'] = True

            rank.append(tmp)
        sorted_rank = sorted(rank, key=(lambda x: -x['win_rate']))
        return sorted_rank



def create_game(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logger = logging.getLogger('test')
            logger.error(request.POST)

            logger.error(request.POST.get('num_players'))
            num_player = int(request.POST.get('num_players'))
            game = Game(num_players=num_player)
            
            scores = []
            for i in range(1,num_player+1):
                player_set = User.objects.filter(username=request.POST.get('player_'+str(i)+'_name'))
                if player_set.exists():
                    player = player_set.get()
                else:
                    raise BadRequest
                intScore = request.POST.get('player_'+str(i)+'_score')
                if i % 2 == 1:
                    win = True
                else:
                    win = False
                
                scores.append(Score(game=game, player=player, score=intScore, win=win))
                #need validation
            game.save()
            for score in scores:
                score.save()
        return redirect('/')
    else:
        raise PermissionDenied

