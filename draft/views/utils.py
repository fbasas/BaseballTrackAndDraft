from draft.models import Player, BatterYearLine
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

BATTER_POS_CHOICES = [
    ('ALL', 'ALL'),
    ('C', 'C'),
    ('1B', '1B'),
    ('2B', '2B'),
    ('SS', 'SS'),
    ('3B', '3B'),
    ('OF', 'OF')
]

PITCHER_POS_CHOICES = [
    ('ALL', 'ALL'),
    ('SP', 'SP'),
    ('RP', 'RP')
]

LEAGUE_CHOICES = [
    ('MLB', 'MLB'),
    ('AL', 'AL'),
    ('NL', 'NL')
]

SORTORDER_CHOICES = [
    ('ASC','Ascending'),
    ('DESC', 'Descending')
]

def clear(request):
    Player.objects.all().delete()
    BatterYearLine.objects.all().delete()
    return HttpResponseRedirect('/draft/cleared/')
    
def cleared(request):
    return render_to_response('redirect.html',
                              {
                                'pageTitle' : 'Information',
                                'message' : 'Database Cleared'
                               })

