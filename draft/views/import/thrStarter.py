from django.shortcuts import render_to_response
from django.template.context import RequestContext
from draft.models import Player

def showTeams(request):
    playerLines = Player.objects.all()
    teams = playerLines.values_list('curTeam', flat=True)
    teams = list(set(teams))

    return render_to_response('showTeams.html',
        {
            'teams' : teams,
            'pageTitle' : 'Teams',
            'headerTitle' : 'Show Teams'
        },
        context_instance=RequestContext(request))


def edit(request, team):
    playerLines = Player.objects.all()
    playerLines = playerLines.filter(curTeam__exact=team)
    playerLines = playerLines.order_by('pos')

    return render_to_response('thrAndStarter.html',
        {
            'lines' : playerLines,
            'pageTitle' : 'Edit Player Status',
            'headerTitle' : 'Team Health Report and Starter Status for ' + team
        },
        context_instance=RequestContext(request))

