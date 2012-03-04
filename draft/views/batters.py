from draft.models import BatterYearLine
from django.shortcuts import render_to_response

def show(request, pos, league, orderby):
    batterLines = BatterYearLine.objects.all()
    if (pos == 'OF'):
        batterLines = batterLines.filter(player__pos__contains='F')
    elif (pos != 'ALL'):
        batterLines = batterLines.filter(player__pos__exact=pos)

    if (league != 'MLB'):
        batterLines = batterLines.filter(league__exact=league)

    batterLines = batterLines.order_by('-' + orderby)
    return render_to_response('batterStats.html',
        {
            'batters' : batterLines,
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos
        })