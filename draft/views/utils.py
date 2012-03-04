from draft.models import Player, BatterYearLine
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def clear(request):
    Player.objects.all().delete()
    BatterYearLine.objects.all().delete()
    return HttpResponseRedirect('/draft/cleared/')
    
def cleared(request):
    return render_to_response('redirect.html',
                              {
                                'pageTitle' : 'Information',
                                'message' : 'Database Cleared'
                               })

