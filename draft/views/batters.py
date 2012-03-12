from django import forms
from django.forms.fields import ChoiceField
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from draft.models import BatterYearLine
from django.shortcuts import render_to_response
from draft.views.utils import BATTER_POS_CHOICES, LEAGUE_CHOICES, SORTORDER_CHOICES

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

LINES_PER_PAGE = 20

class batterFilterForm(forms.Form):
    STAT_CHOICES = []

    for entry in batterPecotaConfig:
        STAT_CHOICES.append((entry[1], entry[0]))

    pos = ChoiceField(choices=BATTER_POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    orderby = ChoiceField(choices=STAT_CHOICES, label='Order By')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')

def changeFilter(request):
    form = batterFilterForm(request.POST)
    if form.is_valid():
        urlRedirect = '/batters/find/{pos}/{league}/{orderby}/{sortorder}/1'.format(
            pos=form.cleaned_data['pos'],
            league=form.cleaned_data['league'],
            orderby=form.cleaned_data['orderby'],
            sortorder=form.cleaned_data['sortorder']
        )
        return HttpResponseRedirect(urlRedirect)

def show(request, pos, league, orderby, sortorder, page):
    batterLines = BatterYearLine.objects.all()
    if pos == 'OF':
        batterLines = batterLines.filter(player__pos__contains='F')
    elif pos != 'ALL':
        batterLines = batterLines.filter(player__pos__exact=pos)

    if league != 'MLB':
        batterLines = batterLines.filter(league__exact=league)

    if sortorder == 'ASC':
        batterLines = batterLines.order_by(orderby)
    else:
        batterLines = batterLines.order_by('-' + orderby)

    form = batterFilterForm(initial=
        {
            'pos' : pos,
            'league' : league,
            'orderby' : orderby,
            'sortorder' : sortorder
        })

    start = LINES_PER_PAGE * (int(page) - 1)
    end = LINES_PER_PAGE * int(page) - 1
    numPages = len(batterLines) / LINES_PER_PAGE + 1

    return render_to_response('stats.html',
        {
            'lines' : batterLines[start:end],
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos,
            'config' : batterPecotaConfig,
            'form' : form,
            'filterAction' : '/draft/batters/changeFilter',
            'baseUrl' : '/batters/find/{pos}/{league}/{orderby}/{sortorder}'.format(
                pos=pos,
                league=league,
                orderby=orderby,
                sortorder=sortorder
            ),
            'activePage' : page,
            'numPages' : numPages
        },
        context_instance=RequestContext(request))