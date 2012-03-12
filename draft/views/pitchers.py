from django import forms
from django.forms.fields import ChoiceField
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from draft.models import PitcherYearLine
from django.shortcuts import render_to_response
from django.db.models import F
from draft.views.batters import LINES_PER_PAGE
from draft.views.utils import PITCHER_POS_CHOICES, LEAGUE_CHOICES, SORTORDER_CHOICES

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

class pitcherFilterForm(forms.Form):
    STAT_CHOICES = []

    for entry in pitcherPecotaConfig:
        STAT_CHOICES.append((entry[1], entry[0]))

    pos = ChoiceField(choices=PITCHER_POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    orderby = ChoiceField(choices=STAT_CHOICES, label='Order By')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')

def changeFilter(request):
    form = pitcherFilterForm(request.POST)
    if form.is_valid():
        urlRedirect = '/pitchers/find/{pos}/{league}/{orderby}/{sortorder}/1'.format(
            pos=form.cleaned_data['pos'],
            league=form.cleaned_data['league'],
            orderby=form.cleaned_data['orderby'],
            sortorder=form.cleaned_data['sortorder']
        )

        return HttpResponseRedirect(urlRedirect)

def show(request, pos, league, orderby, sortorder, page):
    pitcherLines = PitcherYearLine.objects.all()
    if pos == 'SP':
        pitcherLines = pitcherLines.filter(games__lte=F('gamesStarted') * 2)
    elif pos == 'RP':
        pitcherLines = pitcherLines.filter(games__gt=F('gamesStarted') * 2)

    if league != 'MLB':
        pitcherLines = pitcherLines.filter(league__exact=league)

    if sortorder == 'ASC':
        pitcherLines = pitcherLines.order_by(orderby)
    else:
        pitcherLines = pitcherLines.order_by('-' + orderby)

    form = pitcherFilterForm(initial=
        {
            'pos' : pos,
            'league' : league,
            'orderby' : orderby,
            'sortorder' : sortorder
        })

    start = LINES_PER_PAGE * (int(page) - 1)
    end = LINES_PER_PAGE * int(page) - 1
    numPages = len(pitcherLines) / LINES_PER_PAGE + 1

    return render_to_response('stats.html',
        {
            'lines' : pitcherLines[start:end],
            'pageTitle' : 'Pitcher Stats for ' + pos,
            'headerTitle' : 'Pitcher lines for pos: ' + pos,
            'pos' : pos,
            'config' : pitcherPecotaConfig,
            'form' : form,
            'filterAction' : 'draft/pitchers/changeFilter',
            'baseUrl' : '/pitchers/find/{pos}/{league}/{orderby}/{sortorder}'.format(
                pos=pos,
                league=league,
                orderby=orderby,
                sortorder=sortorder
            ),
            'activePage' : page,
            'numPages' : numPages
         },
        context_instance=RequestContext(request))
