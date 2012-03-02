from draft.models import BatterYearLine
from django.shortcuts import render_to_response

def show(request, pos, league):
    if (pos == 'OF'):
        batterLines = BatterYearLine.objects.filter(player__pos__contains='F')
    else:
        batterLines = BatterYearLine.objects.filter(player__pos__exact=pos)

    if (league != 'MLB'):
        batterLines = batterLines.filter(league__exact=league)

    batterLines = batterLines.order_by('-vorp')
    return render_to_response('stats.html',
        {
            'batters' : batterLines,
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos
        })