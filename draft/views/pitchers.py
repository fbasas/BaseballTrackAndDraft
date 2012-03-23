from django import forms
from django.forms.fields import ChoiceField
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from draft.models import PitcherYearLine, League, DraftPick
from django.shortcuts import render_to_response
from django.db.models import F
from draft.views.batters import LINES_PER_PAGE
from draft.views.utils import PITCHER_POS_CHOICES, LEAGUE_CHOICES, SORTORDER_CHOICES, getTeamToDraft, YESNO_CHOICES

pitcherPecotaConfig = [
    ('Line', 'fullLabel'),
    ('Name', 'player.fullName'),
    ('Age', 'age'),
    ('Team', 'team'),
    ('League', 'league'),
    ('Pos', 'player.pos'),
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
    ('FRA', 'fairRa', 2),
    ('WHIP', 'whip', 3),
    ('BB9', 'bb9', 1),
    ('K9', 'k9', 1),
    ('K/BB', 'kbbRatio', 2),
    ('WARP', 'warp', 1)
]

pitcherBbhqConfig = [
    ('Line', 'fullLabel'),
    ('Name', 'player.fullName'),
    ('Age', 'age'),
    ('Team', 'team'),
    ('Pos', 'player.pos'),
    ('$', 'dollarValue'),
    ('MM', 'mmCode'),
    ('G', 'games'),
    ('QS', 'qualityStarts'),
    ('IP', 'inningsPitched', 1),
    ('W', 'wins'),
    ('SV', 'saves'),
    ('H', 'hitsAllowed'),
    ('BB', 'walksAllowed'),
    ('SO', 'strikeouts'),
    ('ERA', 'era', 2),
    ('xERA', 'xera', 2),
    ('WHIP', 'whip', 3),
    ('BB9', 'bb9', 1),
    ('K9', 'k9', 1),
    ('K/BB', 'kbbRatio', 2),
    ('G%', 'groundBallRatio'),
    ('L%', 'lineDriveRatio'),
    ('F%', 'flyBallRatio'),
    ('H%', 'hitRatio'),
    ('BPV', 'bpv')
]

class pitcherFilterForm(forms.Form):
    STAT_CHOICES = []

    for entry in pitcherPecotaConfig:
        STAT_CHOICES.append((entry[1], entry[0]))

    pos = ChoiceField(choices=PITCHER_POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    orderby = ChoiceField(choices=STAT_CHOICES, label='Order By')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')
    showdrafted = ChoiceField(choices=YESNO_CHOICES, label='Show Drafted Players')

def changeFilter(request):
    form = pitcherFilterForm(request.POST)
    if form.is_valid():
        urlRedirect = '/pitchers/find/{pos}/{league}/{orderby}/{sortorder}/1/{showdrafted}'.format(
            pos=form.cleaned_data['pos'],
            league=form.cleaned_data['league'],
            orderby=form.cleaned_data['orderby'],
            sortorder=form.cleaned_data['sortorder'],
            showdrafted=form.cleaned_data['showdrafted']
        )

        return HttpResponseRedirect(urlRedirect)

def show(request, pos, league, orderby, sortorder, page, showdrafted):
    pitcherLines = PitcherYearLine.objects.all()

    hasProjectionType = request.session.__contains__('projectionType')
    if not hasProjectionType:
        request.session['projectionType'] = 'pecota'

    if request.session['projectionType'] == 'pecota':
        pitcherLines = pitcherLines.filter(label__exact='PECOTA Proj')
        if league != 'MLB':
            pitcherLines = pitcherLines.filter(league__exact=league)
    elif request.session['projectionType'] == 'bbhq':
        pitcherLines = pitcherLines.filter(label__exact='BBHQ Proj')

        if orderby == 'warp':
            orderby = 'dollarValue'

    if pos != 'ALL':
        pitcherLines = pitcherLines.filter(player__pos__exact=pos)

    if sortorder == 'ASC':
        pitcherLines = pitcherLines.order_by(orderby)
    else:
        pitcherLines = pitcherLines.order_by('-' + orderby)

    form = pitcherFilterForm(initial=
        {
            'pos' : pos,
            'league' : league,
            'orderby' : orderby,
            'sortorder' : sortorder,
            'showdrafted' : showdrafted
        })

    start = LINES_PER_PAGE * (int(page) - 1)
    end = LINES_PER_PAGE * int(page) - 1
    numPages = len(pitcherLines) / LINES_PER_PAGE + 1

    hasLeagueId = request.session.__contains__('leagueId')
    if hasLeagueId:
        draft = True
        leagueId = request.session['leagueId']
        teamToDraft = getTeamToDraft(leagueId,
            DraftPick.objects.all().count() + 1)[0]
    else:
        draft = False
        leagueId = -1
        teamToDraft = None

    if request.session['projectionType'] == 'pecota':
        config = pitcherPecotaConfig
    elif request.session['projectionType'] == 'bbhq':
        config = pitcherBbhqConfig

    return render_to_response('stats.html',
        {
            'lines' : pitcherLines[start:end],
            'pageTitle' : 'Pitcher Stats for ' + pos,
            'headerTitle' : 'Pitcher lines for pos: ' + pos,
            'pos' : pos,
            'config' : config,
            'form' : form,
            'filterAction' : 'draft/pitchers/changeFilter',
            'baseUrl' : '/pitchers/find/{pos}/{league}/{orderby}/{sortorder}'.format(
                pos=pos,
                league=league,
                orderby=orderby,
                sortorder=sortorder
            ),
            'activePage' : page,
            'numPages' : numPages,
            'draft' : draft,
            'teamToDraft' : teamToDraft,
            'leagueId' : leagueId,
            'showdrafted' : showdrafted
         },
        context_instance=RequestContext(request))
