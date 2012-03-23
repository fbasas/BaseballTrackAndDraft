from django import forms
from django.forms.fields import ChoiceField
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from draft.models import DraftPick, League, Team, Player
from draft.views.utils import BATTER_POS_CHOICES, SORTORDER_CHOICES

draftPickConfig = [
    ('Pick', 'pick'),
    ('Position', 'player.pos'),
    ('Name', 'player.fullName'),
    ('Team', 'team.fullName')
]

LINES_PER_PAGE = 20

class draftPickFilterForm(forms.Form):
    STAT_CHOICES = []

    for entry in draftPickConfig:
        STAT_CHOICES.append((entry[1], entry[0]))

    ALL_POS_CHOICES = []

    for entry in BATTER_POS_CHOICES:
        ALL_POS_CHOICES.append((entry[0], entry[1]))

    ALL_POS_CHOICES.append(('SP', 'SP'))
    ALL_POS_CHOICES.append(('RP', 'RP'))

    LEAGUE_CHOICES = []

    leagues = League.objects.all()
    for league in leagues:
        LEAGUE_CHOICES.append((str(league.id), league.name))

    pos = ChoiceField(choices=ALL_POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    orderby = ChoiceField(choices=STAT_CHOICES, label='Order By')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')

def changeFilter(request):
    form = draftPickFilterForm(request.POST)
    if form.is_valid():
        urlRedirect = '/draft/find/{pos}/{league}/{orderby}/{sortorder}/1'.format(
            pos=form.cleaned_data['pos'],
            league=form.cleaned_data['league'],
            orderby=form.cleaned_data['orderby'],
            sortorder=form.cleaned_data['sortorder']
        )

    return HttpResponseRedirect(urlRedirect)

def add(request, player, team, league):
    # Search through draft picks for league and find latest
    picksSoFar = DraftPick.objects.all()
    picksSoFar = picksSoFar.filter(league__exact = league).order_by('-pick')

    if picksSoFar.count() == 0:
        # No picks in this league yet
        newPick = DraftPick(league = League.objects.get(id=int(league)),
            team = Team.objects.get(id=int(team)),
            player = Player.objects.get(id=int(player)), pick = 1)
    else:
        latestPick = picksSoFar[0]
        newPick = DraftPick(league = League.objects.get(id=int(league)),
            team = Team.objects.get(id=int(team)),
            player = Player.objects.get(id=int(player)),
            pick = latestPick.pick + 1)

    newPick.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def show(request, pos, league, orderby, sortorder, page):
    picksLines = DraftPick.objects.all()
    if pos == 'OF':
        picksLines = picksLines.filter(player__pos__contains='F')

    picksLines = picksLines.filter(league__exact=league)

    return render_to_response('stats.html',
        {

        },
        context_instance=RequestContext(request)
    )
