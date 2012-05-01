from django import forms
from django.forms.fields import ChoiceField
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from draft.models import BatterYearLine, League, DraftPick
from django.shortcuts import render_to_response
from draft.views.utils import BATTER_POS_CHOICES, LEAGUE_CHOICES, SORTORDER_CHOICES, getTeamToDraft, YESNO_CHOICES

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

batterBbhqConfig = [
    ('Line', 'fullLabel'),
    ('Name', 'player.fullName'),
    ('Age', 'age'),
    ('Team', 'team'),
    ('Pos', 'player.pos'),
    ('$', 'dollarValue'),
    ('MM', 'mmCode'),
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
    ('BB%', 'bbRatio'),
    ('Ct%', 'contactRatio', 2),
    ('Eye', 'eye'),
    ('PX', 'px'),
    ('G%', 'groundBallRatio'),
    ('L%', 'lineDriveRatio'),
    ('F%', 'flyBallRatio'),
    ('XBA', 'xba'),
    ('BPV', 'bpv')
]

LINES_PER_PAGE = 20

class batterFilterForm(forms.Form):
    pos = ChoiceField(choices=BATTER_POS_CHOICES, label='Position')
    league = ChoiceField(choices=LEAGUE_CHOICES, label='League')
    sortorder = ChoiceField(choices=SORTORDER_CHOICES, label='Sort Order')
    showdrafted = ChoiceField(choices=YESNO_CHOICES, label='Show Drafted Players')

    def __init__(self, config=None, *args, **kwargs):
        STAT_CHOICES = []

        if config is not None:
            super(batterFilterForm, self).__init__(*args, **kwargs)
            for entry in config:
                STAT_CHOICES.append((entry[1], entry[0]))
            self.fields['orderby'] = ChoiceField(choices=STAT_CHOICES, label='Order By')
        else:
            super(batterFilterForm, self).__init__(*args, **kwargs)
            STAT_CHOICES.append((kwargs['data']['orderby'], kwargs['data']['orderby']))
            self.fields['orderby'] = ChoiceField(choices=STAT_CHOICES, label='Order By')

    def clean(self):
        cleaned_data = super(batterFilterForm, self).clean()
        cleaned_data['orderby'] = self.data['orderby']

        return cleaned_data

def changeFilter(request):
    form = batterFilterForm(data=request.POST)
    if form.is_valid():
        urlRedirect = '/batters/find/{pos}/{league}/{orderby}/{sortorder}/1/{showdrafted}'.format(
            pos=form.cleaned_data['pos'],
            league=form.cleaned_data['league'],
            orderby=form.cleaned_data['orderby'],
            sortorder=form.cleaned_data['sortorder'],
            showdrafted=form.cleaned_data['showdrafted']
        )
        return HttpResponseRedirect(urlRedirect)

def show(request, pos, league, orderby, sortorder, page, showdrafted):
    batterLines = BatterYearLine.objects.all()

    if showdrafted == '0':
        batterLines = batterLines.exclude(player__draftpick__isnull = False)

    hasProjectionType = request.session.__contains__('projectionType')
    if not hasProjectionType:
        request.session['projectionType'] = 'pecota'

    if pos == 'OF':
        batterLines = batterLines.filter(player__pos__contains='F')
    elif pos != 'ALL':
        batterLines = batterLines.filter(player__pos__exact=pos)

    if request.session['projectionType'] == 'pecota':
        batterLines = batterLines.filter(label__exact='PECOTA Proj')

        if league != 'MLB':
            batterLines = batterLines.filter(league__exact=league)
    else:
        batterLines = batterLines.filter(label__exact='BBHQ Proj')
        if orderby == 'vorp':
            orderby = 'dollarValue'

    if sortorder == 'ASC':
        batterLines = batterLines.order_by(orderby)
    else:
        batterLines = batterLines.order_by('-' + orderby)

    currentConfig = []

    if request.session['projectionType'] == 'pecota':
        currentConfig = batterPecotaConfig
    elif request.session['projectionType'] == 'bbhq':
        currentConfig = batterBbhqConfig

    form = batterFilterForm(currentConfig, data=
        {
            'pos' : pos,
            'league' : league,
            'orderby' : orderby,
            'sortorder' : sortorder,
            'showdrafted' : showdrafted
        })

    start = LINES_PER_PAGE * (int(page) - 1)
    end = LINES_PER_PAGE * int(page)

    numPages = len(batterLines) / LINES_PER_PAGE + 1

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

    return render_to_response('stats.html',
        {
            'lines' : batterLines[start:end],
            'pageTitle' : 'Batter Stats for ' + pos,
            'headerTitle' : 'Batter lines for pos: ' + pos,
            'pos' : pos,
            'config' : currentConfig,
            'form' : form,
            'filterAction' : '/draft/batters/changeFilter',
            'baseUrl' : '/batters/find/{pos}/{league}/{orderby}/{sortorder}'.format(
                pos=pos,
                league=league,
                orderby=orderby,
                sortorder=sortorder
            ),
            'activePage' : page,
            'numPages' : numPages,
            'draft' : draft,
            'teamToDraft' : teamToDraft,
            'leagueId' : int(leagueId),
            'showdrafted' : showdrafted
        },
        context_instance=RequestContext(request))