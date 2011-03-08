from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 
from django.http import HttpResponse
from things.models import Thing

def index(request):
    things = Thing.objects.all()
    return render_to_response('things/thing_list.html', {'things': things})

def show(request, thing_slug):
    thing = get_object_or_404(Thing, slug=thing_slug)
    return render_to_response('things/thing_detail.html', {'thing': thing}, 
        context_instance = RequestContext(request))
