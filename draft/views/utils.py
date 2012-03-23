from draft.models import Player, BatterYearLine, League, Team
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

BATTER_POS_CHOICES = [
    ('ALL', 'ALL'),
    ('C', 'C'),
    ('1B', '1B'),
    ('2B', '2B'),
    ('SS', 'SS'),
    ('3B', '3B'),
    ('OF', 'OF')
]

PITCHER_POS_CHOICES = [
    ('ALL', 'ALL'),
    ('SP', 'SP'),
    ('RP', 'RP')
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

YESNO_CHOICES = [
    ('1', 'Yes'),
    ('0', 'No')
]

def clearPecota(request):
    Player.objects.all().filter(importMethod__exact='PECOTA').delete()
    BatterYearLine.objects.all().filter(label__exact='PECOTA Proj').delete()
    return HttpResponseRedirect('/draft/cleared')

def clearBbhq(request):
    Player.objects.all().filter(importMethod__exact='BBHQ').delete()
    BatterYearLine.objects.all().filter(label__exact='BBHQ Proj').delete()
    return HttpResponseRedirect('/draft/cleared')
    
def cleared(request):
    return render_to_response('redirect.html',
                              {
                                'pageTitle' : 'Information',
                                'message' : 'Database Cleared'
                               })

def setProjection(request, projectionType):
    request.session['projectionType'] = projectionType
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def setLeague(request, leagueId):
    request.session['leagueId'] = leagueId
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def getTeamToDraft(leagueId, draftNum):
    if leagueId == -1:
        return -1

    numTeams = Team.objects.all().filter(league = leagueId).count()

    if draftNum % numTeams == 0:
        round = draftNum / numTeams
    else:
        round = draftNum / numTeams + 1

    if round % 2 == 0:
        positionToPick = numTeams + 1 - (draftNum - (round - 1) * numTeams)
    else:
        positionToPick = draftNum - (round - 1) * numTeams

    return Team.objects.all().filter(league = leagueId).filter(draftPosition = positionToPick)

