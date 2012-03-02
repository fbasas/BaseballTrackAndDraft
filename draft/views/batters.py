from draft.models import BatterYearLine
from django.shortcuts import render_to_response

def show(request, pos):
    batterLines = BatterYearLine.objects.filter(player__pos__exact=pos)
    return render_to_response('stats.html',
        {
            'batters' : batterLines,
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos
        })