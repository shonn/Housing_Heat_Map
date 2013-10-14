from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from HeatMap.models import HouseData

def home(request):
    p = "none"#HouseData.objects.filter(house_zip=95129)
    return render_to_response('results.html', {'house': p})

def zip(request, zip):
    p = HouseData.objects.filter(house_zip=zip)
    return render_to_response('results.html', {'house': p})
    