from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect

from draft.models import Player, BatterYearLine, PitcherYearLine
import csv

def index(request):
    if request.method == 'POST':
        processBbhqBatterFile(request.FILES['bbhq_batter_CSV_file'])
        processBbhqPitcherFile(request.FILES['bbhq_pitcher_CSV_file'])
        return HttpResponseRedirect('/draft/import/bbhq/importfinished')
    else:
        form = bbhqUploadForm()

    return render_to_response('import.html',
            {
            'form' : form,
            'importType' : 'bbhq',
            'pageTitle' : 'BBHQ Import',
            'headerTitle' : 'Welcome to BBHQ Import'
        },
        context_instance=RequestContext(request))

def importFinished(request):
    return render_to_response('redirect.html',
            {
            'pageTitle' : 'Import Completed',
            'message' : 'BBHQ Batter and Pitcher CSV import completed'
        })

class bbhqUploadForm(forms.Form):
    bbhq_batter_CSV_file = forms.FileField()
    bbhq_pitcher_CSV_file = forms.FileField()

def processBbhqPitcherFile(pitcherFile):
    reader = csv.DictReader(pitcherFile)
    for line in reader:
        first_name = line['Firstname']
        last_name = line['Lastname']

        # Do we have this player already?
        playerSet = Player.objects.filter(firstName = first_name, lastName = last_name)
        if not playerSet.count():
            # No player found, so add one
            newPlayer = Player(firstName = first_name, lastName = last_name, importMethod = 'BBHQ')
            newPlayer.save()
            addBbhqPitcherLine(line, newPlayer)
        else:
            addBbhqPitcherLine(line, playerSet[0])

def addBbhqPitcherLine(line, player):
    newPitcher = PitcherYearLine()
    newPitcher.player = player
    newPitcher.label = 'BBHQ Proj'
    newPitcher.yearLabel = '2012'
    newPitcher.age = line['Age']
    newPitcher.team = line['Tm']
    newPitcher.mmCode = line['MM Code']
    newPitcher.dlDays = line['DL']
    newPitcher.inningsPitched = line['IP']
    newPitcher.era = line['ERA']
    newPitcher.xera = line['xERA']
    newPitcher.hitsAllowed = line['H']
    newPitcher.earnedRuns = line['ER']
    newPitcher.walksAllowed = line['BB']
    newPitcher.strikeouts = line['K']
    newPitcher.wins = line['W']
    newPitcher.saves = line['Sv']
    newPitcher.dollarValue = line['12$']
    newPitcher.games = line['G']
    newPitcher.qualityStarts = line['QS']
    newPitcher.whip = line['WHIP']
    newPitcher.bb9 = line['BB9']
    newPitcher.k9 = line['K9']
    newPitcher.kbbRatio = float(newPitcher.strikeouts) / float(newPitcher.walksAllowed)
    newPitcher.groundBallRatio = line['G%']
    newPitcher.lineDriveRatio = line['L%']
    newPitcher.flyBallRatio = line['F%']
    newPitcher.hitRatio = line['H%']
    newPitcher.bpv = line['BPV']

    newPitcher.player.save()
    newPitcher.save()

def processBbhqBatterFile(batterFile):
    reader = csv.DictReader(batterFile)
    for line in reader:
        first_name = line['Firstname']
        last_name = line['Lastname']
        pos = line['Pos']

        # Do we have this player already?
        playerSet = Player.objects.filter(firstName = first_name, lastName = last_name)
        if not playerSet.count():
            # No player found, so add one
            newPlayer = Player(firstName = first_name, lastName = last_name, importMethod = 'BBHQ',
                pos = pos)
            newPlayer.save()
            addBbhqBatterLine(line, newPlayer)
        else:
            addBbhqBatterLine(line, playerSet[0])

def addBbhqBatterLine(line, player):
    newBatter = BatterYearLine()
    newBatter.player = player
    newBatter.label = 'BBHQ Proj'
    newBatter.yearLabel = '2012'
    newBatter.age = line['Age']
    newBatter.mmCode = line['MM Code']
    newBatter.dlDays = line['DL']
    newBatter.atBats = line['AB']
    newBatter.team = line['Tm']
    newBatter.hits = line['H']
    newBatter.doubles = line['2B']
    newBatter.triples = line['3B']
    newBatter.homeRuns = line['HR']
    newBatter.runs = line['R']
    newBatter.rbi = line['RBI']
    newBatter.walks = line['BB']
    newBatter.strikeouts = line['K']
    newBatter.stolenBases = line['SB']
    newBatter.dollarValue = line['12$']
    newBatter.avg = float(line['AVG']) / 1000.0
    newBatter.obp = float(line['OBP']) / 1000.0
    newBatter.slg = float(line['SLG']) / 1000.0
    newBatter.bbRatio = line['BB%']
    newBatter.contactRatio = float(line['Ct%']) / 100.0
    newBatter.eye = line['Eye']
    newBatter.px = line['PX']
    newBatter.groundBallRatio = line['G%']
    newBatter.lineDriveRatio = line['L%']
    newBatter.flyBallRatio = line['F%']
    newBatter.xba = float(line['XBA']) / 1000.0
    newBatter.bpv = line['BPV']
    newBatter.save()
