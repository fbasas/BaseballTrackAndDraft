from draft.models import PitcherYearLine
from django.shortcuts import render_to_response
from django.db.models import F

pitcherPecotaConfig = [
    ('Line', 'fullLabel'),
    ('Name', 'player.fullName'),
    ('Age', 'age'),
    ('Team', 'team'),
    ('League', 'league'),
    ('G', 'games'),
    ('GS', 'gamesStarted'),
    ('QS', 'qualityStarts'),
    ('IP', 'inningsPitched', 1),
    ('W', 'wins'),
    ('SV', 'saves'),
    ('H', 'hitsAllowed'),
    ('BB', 'walksAllowed'),
    ('SO', 'strikeouts'),
    ('ERA', 'era', 2),
    ('FAIRRA', 'fairRa', 2),
    ('WHIP', 'whip', 3),
    ('BB9', 'bb9', 1),
    ('K9', 'k9', 1),
    ('K/BB', 'kbbRatio', 2),
    ('WARP', 'warp', 1)
]

def show(request, pos, league, orderby):
    pitcherLines = PitcherYearLine.objects.all()
    if (pos == 'SP'):
        pitcherLines = pitcherLines.filter(games__lte=F('gamesStarted') * 2)
    elif (pos == 'RP'):
        pitcherLines = pitcherLines.filter(games__gt=F('gamesStarted') * 2)

    if (league != 'MLB'):
        pitcherLines = pitcherLines.filter(league__exact=league)

    pitcherLines = pitcherLines.order_by('-' + orderby)
    return render_to_response('stats.html',
        {
            'lines' : pitcherLines,
            'pageTitle' : 'Pitcher Stats for ' + pos,
            'headerTitle' : 'Pitcher lines for pos: ' + pos,
            'pos' : pos,
            'config' : pitcherPecotaConfig
        })
