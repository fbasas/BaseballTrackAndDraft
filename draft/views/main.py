from django.shortcuts import render_to_response
from django.template.context import RequestContext

def show(request):
    return render_to_response('main.html', {},
        context_instance=RequestContext(request))
