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
    
def price_growth_in_bounding_box_to_geojson(request):
	querystr = '''select gid, zcta5ce10, ST_asGeoJSON(geom) as json
					from zipcodeshapes 
					WHERE ST_intersects(geom, 
						ST_GeomFromText('Polygon((-122.110097522937 37.410954310473784, 
											-122.06074487706297 37.410954310473784, 
											-122.06074487706297 37.4348799782838, 
											-122.110097522937 37.4348799782838, 
											-122.110097522937 37.410954310473784))',4269))
				'''
	shapes = Zipcodeshapes.objects.raw(querystr)
	context = {'shapes':shapes}
	for s in shapes:
		print(s.json)
	return render(request, 'HeatMap/GeoJSON.json', context)
	
def zip_code_test(request):
	context = {}
	return render(request, 'HeatMap/ZipCodeTest.html', context)
	
def geojson_js_parser(request):
	context = {}
	return render(request, 'HeatMap/GeoJSON.js', context)