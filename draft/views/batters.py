from django import forms
from django.forms.fields import ChoiceField
from django.template.context import RequestContext
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

class batterFilterForm(forms.Form):
    POS_CHOICES = [
        ('ALL', 'ALL'),
        ('C', 'C'),
        ('1B', '1B'),
        ('2B', '2B'),
        ('SS', 'SS'),
        ('3B', '3B'),
        ('OF', 'OF')
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

    STAT_CHOICES = []

    for entry in batterPecotaConfig:
        STAT_CHOICES.append((entry[1], entry[0]))

    pos = ChoiceField(choices=POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    orderby = ChoiceField(choices=STAT_CHOICES, label='Order By')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')

def changeFilter(request):
    form = batterFilterForm(request.POST)
    if form.is_valid():
        return show(request,
            form.cleaned_data['pos'],
            form.cleaned_data['league'],
            form.cleaned_data['orderby'],
            form.cleaned_data['sortorder'])

def show(request, pos, league, orderby, sortorder):
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

    return render_to_response('stats.html',
        {
            'lines' : batterLines,
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos,
            'config' : batterPecotaConfig,
            'form' : form
        },
        context_instance=RequestContext(request))