from draft.models import League

def default(request):
    if 'leagueId' not in request.session.keys():
        leagueName = 'None'
        leagueId = -1
    else:
        leagueName = League.objects.get(id=request.session['leagueId']).name
        leagueId = request.session['leagueId']

    if 'projectionType' not in request.session.keys():
        projectionType = 'PECOTA'
    else:
        projectionType = request.session['projectionType']

    return {'leagueId': leagueId,
            'leagues' : League.objects.all(),
            'leagueName' : leagueName,
            'projectionType' : projectionType}
