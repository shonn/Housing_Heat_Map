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
	data_things = []
	try:
		southLatitude = request.GET['southLatitude']
		westLongitude = request.GET['westLongitude']
		eastLongitude = request.GET['eastLongitude']
		northLatitude = request.GET['northLatitude']
		box_wkt='Polygon((' + westLongitude + ' ' + southLatitude + ','
		box_wkt+= westLongitude + ' ' + northLatitude + ','
		box_wkt+= eastLongitude + ' ' + northLatitude + ','
		box_wkt+= eastLongitude + ' ' + southLatitude + ','
		box_wkt+= westLongitude + ' ' + southLatitude + '))'
		shapes = Zipcodeshapes.objects.filter(geom__intersects = box_wkt)
		year1 = request.GET['year1']
		year2 = request.GET['year2']
		for shape in shapes:
			try:
				price1 = HouseData.objects.get(house_zip=shape.zcta5ce10, house_date__year = year1).house_price
				price2 = HouseData.objects.get(house_zip=shape.zcta5ce10, house_date__year = year2).house_price
				data_things.append({'shape':shape.geom.geojson, 
					'name':shape.zcta5ce10, 
					'type': 'price_growth',
					'value': (price2-price1)/price1})
			except(HouseData.DoesNotExist):
				continue
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
		context={'data': data_things}
		return render(request, 'HeatMap/GeoJSON.json', context)

def zip_code_test(request):
	context = {}
	return render(request, 'HeatMap/ZipCodeTest.html', context)
	
def geojson_js_parser(request):
	context = {}
	return render(request, 'HeatMap/GeoJSON.js', context)