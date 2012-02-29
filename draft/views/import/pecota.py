from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect

from draft.models import Player, BatterYearLine
import csv

def index(request):
    if request.method == 'POST':
        processPecotaBatterFile(request.FILES['pecota_batter_CSV_file'])
        return HttpResponseRedirect('/draft/import/pecota/battersfinished')
    else:
        form = pecotaUploadForm()
        
    return render_to_response('import.html',
                              {
                               'form' : form,
                               'pageTitle' : 'PECOTA Import',
                               'headerTitle' : 'Welcome to PECOTA Import'
                               },
                              context_instance=RequestContext(request))
    
def battersFinished(request):
    return render_to_response('redirect.html',
                              {
                                'pageTitle' : 'Import Completed',
                                'message' : 'PECOTA Batter CSV import completed'
                               })
    
class pecotaUploadForm(forms.Form):
    pecota_batter_CSV_file = forms.FileField()
    
def processPecotaBatterFile(batterFile):
    reader = csv.DictReader(batterFile)
    for line in reader:
        first_name = line['FIRSTNAME']
        last_name = line['LASTNAME']
        bpid = line['BPID']
        mlbid = line['MLBCODE']
        pos = line['POS']
        
        # Do we have this player already?
        playerSet = Player.objects.filter(firstName = first_name, lastName = last_name)
        if playerSet.count() == 0:
            # No player found, so add one
            newPlayer = Player(firstName = first_name, lastName = last_name, importMethod = 'PECOTA',
                               bpId = bpid, mlbId = mlbid, pos = pos)
            newPlayer.save()
            
            addPecotaBatterLine(line, newPlayer)
            
def addPecotaBatterLine(line, player):
    newBatter = BatterYearLine ()
    newBatter.player = player
    newBatter.label = 'PECOTA Proj'
    newBatter.yearLabel = '2012'
    newBatter.age = line['AGE']
    newBatter.atBats = line['AB']
    newBatter.team = line['TEAM']
    newBatter.hits = line['H']
    newBatter.doubles = line['2B']
    newBatter.triples = line['3B']
    newBatter.homeRuns = line['HR']
    newBatter.runs = line['R']
    newBatter.rbi = line['RBI']
    newBatter.walks = line['BB']
    newBatter.strikeouts = line['SO']
    newBatter.stolenBases = line['SB']
    newBatter.save()
    
    