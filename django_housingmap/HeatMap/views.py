from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from HeatMap.models import HouseData, Zipcodeshapes

def home(request):
    p = "none"#HouseData.objects.filter(house_zip=95129)
    return render_to_response('results.html', {'house': p})

def zip(request, zip):
    p = HouseData.objects.filter(house_zip=zip)
    return render_to_response('results.html', {'house': p})
    
def price_growth_in_bounding_box_to_geojson_form(request):
	context = {'action': 'price_growth_in_bounding_box_to_geojson',
		'westLongitude': -122.110097522937,
		'eastLongitude': -122.06074487706297,
		'northLatitude': 37.4348799782838,
		'southLatitude': 37.410954310473784,}
	return render(request, 'HeatMap/BoxTest.html', context)  
	  
def price_growth_in_bounding_box_to_geojson(request):
	try:
		westLongitude = request.POST['westLongitude']
		eastLongitude = request.POST['eastLongitude']
		northLatitude = request.POST['northLatitude']
		southLatitude = request.POST['southLatitude']
		box_wkt='Polygon((' + westLongitude + ' ' + southLatitude + ','
		box_wkt+= westLongitude + ' ' + northLatitude + ','
		box_wkt+= eastLongitude + ' ' + northLatitude + ','
		box_wkt+= eastLongitude + ' ' + southLatitude + ','
		box_wkt+= westLongitude + ' ' + southLatitude + '))'
		shapes = Zipcodeshapes.objects.filter(geom__intersects = box_wkt)
	except (KeyError):
		return price_growth_in_bounding_box_to_geojson_form(request)
	except (Zipcodeshapes.DoesNotExist, ValueError):
		return render(request, 'HeatMap/BoxTest.html', {
			'action':'price_growth_in_bounding_box_to_geojson',
			'westLongitude': westLongitude,
			'eastLongitude': eastLongitude,
			'northLatitude': northLatitude,
			'southLatitude': southLatitude,
			'error_message':'There was an error processing your request',
		})
	else:
		context = {'shapes':shapes}
		return render(request, 'HeatMap/GeoJSON.json', context)

def zip_code_test(request):
	context = {}
	return render(request, 'HeatMap/ZipCodeTest.html', context)
	
def geojson_js_parser(request):
	context = {}
	return render(request, 'HeatMap/GeoJSON.js', context)