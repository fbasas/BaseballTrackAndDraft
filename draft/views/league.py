from django import forms
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from draft.models import League, Team

leagueConfig = [
    ('Team', 'teamName'),
    ('Manager', 'managerName')
]

def create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            leagueType = form.cleaned_data['leagueType']
            name = form.cleaned_data['name']
            numTeams = form.cleaned_data['numTeams']

            urlRedirect = '/league/addTeams/' + leagueType + '/' + name + '/' + str(numTeams)
            return HttpResponseRedirect(urlRedirect)
    else:
        form = LeagueForm()

    return render_to_response('form.html',
        {
            'form' : form,
            'pageTitle' : 'New League',
            'headerTitle' : 'Create a New League',
            'action' : '/league/create',
            'submitValue' : 'Create League'
        },
        context_instance=RequestContext(request))

def addTeams(request, leagueType, name, numTeams):
    newLeague = League(leagueType = leagueType, name = name)
    newLeague.save()

    TeamFormSet = formset_factory(TeamForm, extra=int(numTeams))

    return render_to_response('form.html',
        {
            'formset' : TeamFormSet,
            'pageTitle' : 'New League',
            'headerTitle' : 'Add teams to ' + name,
            'action' : '/league/setTeams/' + str(newLeague.id) + '/' + str(numTeams),
            'submitValue' : 'Add teams to ' + name
        },
        context_instance=RequestContext(request))

def setTeams(request, leagueId, numTeams):
    for teamId in range(0, int(numTeams)):
        formTeamFieldName = 'form-' + str(teamId) + '-teamName'
        formManagerFieldName = 'form-' + str(teamId) + '-managerName'
        formDraftPositionFieldName = 'form-' + str(teamId) + '-draftPosition'
        teamName = request.POST[formTeamFieldName]
        managerName = request.POST[formManagerFieldName]
        draftPosition = request.POST[formDraftPositionFieldName]

        newTeam = Team(league = League.objects.get(pk=leagueId),
            teamName = teamName, managerName = managerName, draftPosition = draftPosition)
        newTeam.save()

    return render_to_response('stats.html',
        {
            'lines' : Team.objects.all().filter(league__exact=League.objects.get(pk=leagueId)),
            'pageTitle' : 'League Created',
            'headerTitle' : 'League named ' + League.objects.get(pk=leagueId).name + ' created with ' + str(numTeams) + ' teams',
            'config' : leagueConfig,
            'baseUrl' : '/league/setTeams/{leagueId}/{numTeams}'.format(
                leagueId=leagueId,
                numTeams=numTeams
            ),
            'activePage' : 1,
            'numPages' : 1,
            'draft' : False,
            'teamToDraft' : -1,
            'leagueId' : -1,
            'showdrafted' : 1
        },
        context_instance=RequestContext(request))

class TeamForm(forms.Form):
    teamName = forms.CharField(label="Team")
    managerName = forms.CharField(label="Manager")
    draftPosition = forms.IntegerField()

class LeagueForm(forms.Form):
    LEAGUE_TYPE = (
        ('scoresheet', 'Scoresheet'),
        ('yahoo', 'Yahoo')
    )

    leagueType = forms.ChoiceField(choices=LEAGUE_TYPE)
    name = forms.CharField()
    numTeams = forms.IntegerField(label="# of teams")
