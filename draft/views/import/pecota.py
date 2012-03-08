from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect

from draft.models import Player, BatterYearLine, PitcherYearLine
import csv

def index(request):
    if request.method == 'POST':
        processPecotaBatterFile(request.FILES['pecota_batter_CSV_file'])
        processPecotaPitcherFile(request.FILES['pecota_pitcher_CSV_file'])
        return HttpResponseRedirect('/draft/import/pecota/importfinished')
    else:
        form = pecotaUploadForm()
        
    return render_to_response('import.html',
                              {
                               'form' : form,
                               'pageTitle' : 'PECOTA Import',
                               'headerTitle' : 'Welcome to PECOTA Import'
                               },
                              context_instance=RequestContext(request))
    
def importFinished(request):
    return render_to_response('redirect.html',
                              {
                                'pageTitle' : 'Import Completed',
                                'message' : 'PECOTA Batter and Pitcher CSV import completed'
                               })
    
class pecotaUploadForm(forms.Form):
    pecota_batter_CSV_file = forms.FileField()
    pecota_pitcher_CSV_file = forms.FileField()

def processPecotaPitcherFile(pitcherFile):
    reader = csv.DictReader(pitcherFile)
    for line in reader:
        first_name = line['FIRSTNAME']
        last_name = line['LASTNAME']
        bpid = line['BPID']
        mlbid = line['MLBCODE']

        # Do we have this player already?
        playerSet = Player.objects.filter(firstName = first_name, lastName = last_name)
        if not playerSet.count():
            # No player found, so add one
            newPlayer = Player(firstName = first_name, lastName = last_name, importMethod = 'PECOTA',
                bpId = bpid, mlbId = mlbid)
            newPlayer.save()

            addPecotaPitcherLine(line, newPlayer)

def addPecotaPitcherLine(line, player):
    newPitcher = PitcherYearLine()
    newPitcher.player = player
    newPitcher.label = 'PECOTA Proj'
    newPitcher.yearLabel = '2012'
    newPitcher.age = line['AGE']
    newPitcher.team = line['TEAM']
    newPitcher.league = line['LG']
    newPitcher.inningsPitched = line['IP']
    newPitcher.era = line['ERA']
    newPitcher.hitsAllowed = line['H']
    newPitcher.walksAllowed = line['BB']
    newPitcher.strikeouts = line['SO']
    newPitcher.wins = line['W']
    newPitcher.saves = line['SV']
    newPitcher.fairRa = line['FAIR_RA']
    newPitcher.warp = line['WARP']
    newPitcher.games = line['G']
    newPitcher.gamesStarted = line['GS']
    newPitcher.qualityStarts = line['QS']
    newPitcher.whip = (float(newPitcher.walksAllowed) + float(newPitcher.hitsAllowed)) / float(newPitcher.inningsPitched)
    newPitcher.bb9 = line['BB9']
    newPitcher.k9 = line['SO9']
    newPitcher.kbbRatio = float(newPitcher.strikeouts) / float(newPitcher.walksAllowed)
    newPitcher.save()
    
def processPecotaBatterFile(batterFile):
    reader = csv.DictReader(batterFile)
    for line in reader:
        first_name = line['FIRSTNAME']
        last_name = line['LASTNAME']
        bpid = line['BPID']
        mlbid = line['MLBCODE']
        pos = line['POS'].strip()
        
        # Do we have this player already?
        playerSet = Player.objects.filter(firstName = first_name, lastName = last_name)
        if not playerSet.count():
            # No player found, so add one
            newPlayer = Player(firstName = first_name, lastName = last_name, importMethod = 'PECOTA',
                               bpId = bpid, mlbId = mlbid, pos = pos)
            newPlayer.save()
            
            addPecotaBatterLine(line, newPlayer)
            
def addPecotaBatterLine(line, player):
    newBatter = BatterYearLine()
    newBatter.player = player
    newBatter.label = 'PECOTA Proj'
    newBatter.yearLabel = '2012'
    newBatter.age = line['AGE']
    newBatter.atBats = line['AB']
    newBatter.team = line['TEAM']
    newBatter.league = line['LG']
    newBatter.hits = line['H']
    newBatter.doubles = line['2B']
    newBatter.triples = line['3B']
    newBatter.homeRuns = line['HR']
    newBatter.runs = line['R']
    newBatter.rbi = line['RBI']
    newBatter.walks = line['BB']
    newBatter.strikeouts = line['SO']
    newBatter.stolenBases = line['SB']
    newBatter.totalAvg = line['TAv']
    newBatter.vorp = line['VORP']
    newBatter.avg = line['AVG']
    newBatter.obp = line['OBP']
    newBatter.slg = line['SLG']
    newBatter.totalBases = line['TB']
    newBatter.save()
    
    