from draft.models import BatterYearLine
from django.shortcuts import render_to_response

batterPecotaConfig = [
    ('Line', 'fullLabel'),
    ('Name', 'player.fullName'),
    ('Age', 'age'),
    ('Team', 'team'),
    ('League', 'league'),
    ('Pos', 'player.pos'),
    ('AB', 'atBats'),
    ('Runs', 'runs'),
    ('HR', 'homeRuns'),
    ('RBI', 'rbi'),
    ('SB', 'stolenBases'),
    ('BB', 'walks'),
    ('K', 'strikeouts'),
    ('Avg', 'avg', 3),
    ('OBP', 'obp', 3),
    ('SLG', 'slg', 3),
    ('TAv', 'totalAvg', 3),
    ('VORP', 'vorp', 1)
]

def show(request, pos, league, orderby, sortorder):
    batterLines = BatterYearLine.objects.all()
    if pos == 'OF':
        batterLines = batterLines.filter(player__pos__contains='F')
    elif pos != 'ALL':
        batterLines = batterLines.filter(player__pos__exact=pos)

    if league != 'MLB':
        batterLines = batterLines.filter(league__exact=league)

    if sortorder == 'ASC':
        batterLines = batterLines.filter(orderby)
    else:
        batterLines = batterLines.filter('-' + orderby)

    return render_to_response('stats.html',
        {
            'lines' : batterLines,
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos,
            'config' : batterPecotaConfig
        })