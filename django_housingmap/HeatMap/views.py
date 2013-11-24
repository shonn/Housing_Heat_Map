from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from HeatMap.models import HouseData, Zipcodeshapes
from django.db.models import Avg #aggregation
from django.core.cache import cache #memcached
from chartit import DataPool, Chart #for creating statistical charts

def home(request):
    #p = "none"#HouseData.objects.filter(house_zip=95129)

    #step 1, create a datapol with data we want to retrieve
    housedata = \
            DataPool(
                    series=
                    [{'options': {
                        'source': HouseData.objects.filter(house_zip='95133')},
                        'terms': [
                            'house_zip',
                            'house_price']}
                        ])
    #step 2, create chart object
    cht = Chart(
            datasource = housedata,
            series_options =
                [{'options': {
                    'type': 'line',
                    'stacking': False},
                    'terms': {
                        'house_zip': [
                            'house_price']
                        }}],
                    chart_options = 
                        {'title': {
                            'text': 'House prices of zipcode 95133'},
                            'xAxis': {
                                'title': {
                                    'text': 'Date'}}})
    return render_to_response('results.html', {'housedata': cht})

def zip_growth(request, zipcode, year1, year2):
    year1_avg = HouseData.objects.filter(house_zip=zipcode, house_date__contains=year1).aggregate(Avg('house_price'))
    year2_avg = HouseData.objects.filter(house_zip=zipcode, house_date__contains=year2).aggregate(Avg('house_price'))
    pct_change = ((float(year2_avg) - float(year1_avg)) / float(year1_avg)) * 100
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
                shapes = cache.get(southLatitude + westLongitude + eastLongitude)
                data_things = cache.get(southLatitude + westLongitude + eastLongitude + 'd')
                if not shapes:
                    shapes = Zipcodeshapes.objects.filter(geom__intersects = box_wkt)
                    cache.set(southLatitude + westLongitude + eastLongitude, shapes)
                year1 = request.GET['year1']
                year2 = request.GET['year2']
                if not data_things:
                    data_things = []
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
                    cache.set(southLatitude + westLongitude + eastLongitude + 'd', data_things)
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
