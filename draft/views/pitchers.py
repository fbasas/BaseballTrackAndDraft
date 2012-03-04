from draft.models import PitcherYearLine
from django.shortcuts import render_to_response
from django.db.models import F

def show(request, pos, league, orderby):
    pitcherLines = PitcherYearLine.objects.all()
    if (pos == 'SP'):
        pitcherLines = pitcherLines.filter(games__lte=F('gamesStarted') * 2)
    elif (pos == 'RP'):
        pitcherLines = pitcherLines.filter(games__gt=F('gamesStarted') * 2)

    if (league != 'MLB'):
        pitcherLines = pitcherLines.filter(league__exact=league)

    pitcherLines = pitcherLines.order_by('-' + orderby)
    return render_to_response('pitcherStats.html',
        {
            'pitchers' : pitcherLines,
            'pageTitle' : 'Pitcher Stats for ' + pos,
            'headerTitle' : 'Pitcher lines for pos: ' + pos,
            'pos' : pos
        })
