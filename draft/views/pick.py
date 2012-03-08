from draft.models import DraftPick

def add(request, player, team, league):
    # Search through draft picks for league and find latest
    picksSoFar = DraftPick.objects.all()
    picksSoFar = picksSoFar.filter(league__exact = league).order_by('-pick')

    if picksSoFar.count() == 0:
        # No picks in this league yet
        newPick = DraftPick(league = league, team = team, player = player, pick = 1)
    else:
        latestPick = picksSoFar[0]
        newPick = DraftPick(league = league, team = team, player = player, pick = latestPick.pick + 1)

    newPick.save()
