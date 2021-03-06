from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from HeatMap.models import HouseData, Zipcodeshapes
from django.db.models import Avg #aggregation
from django.core.cache import cache #memcached
import memcache
import pickle
from chartit import DataPool, Chart #for creating statistical charts


mc = memcache.Client(['127.0.0.1:11211'], debug=0)
def home(request):
    housezip = request.GET.get('zip', '95129')
    source = HouseData.objects.filter(house_zip=str(housezip))
    title = 'House prices of zipcode ' + housezip
    housezip = str(housezip)
    #step 1, create a datapol with data we want to retrieve
    source = HouseData.objects.filter(house_zip=housezip)
    try:
        source[1]
    except IndexError:
        title = "No records for zipcode " + housezip
    housedata = \
            DataPool(
                    series=
                    [{'options': {
                        'source': source},
                        'terms': [
                            'house_date', 
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
                        'house_date': [
                            'house_price']
                        }}],
                    chart_options = 
                        {'title': {
                            'text': title},
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
	return render(request, 'BoxTest.html', context)  

def price_growth_in_bounding_box_to_geojson(request):
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
                year = request.GET['year1']
                year1 = str(year)+'-12-31'
                year = request.GET['year2']
                year2 = str(year) + '-12-31'
                data_key = str(southLatitude + westLongitude) + year1 + year2
                data_things = mc.get(data_key)
                if not data_things:
                    data_things = []
                    for shape in shapes:
                            try:
                                    price1 = HouseData.objects.get(house_zip=shape.zcta5ce10, house_date = year1).house_price
                                    price2 = HouseData.objects.get(house_zip=shape.zcta5ce10, house_date = year2).house_price
                                    data_things.append({'shape':shape.geom.geojson, 
                                            'name':shape.zcta5ce10, 
                                            'type': 'price_growth',
                                            'value': (price2-price1)/price1})
                            except(HouseData.DoesNotExist):
                                    continue
                    mc.set(data_key, data_things)
        except (KeyError):
                return price_growth_in_bounding_box_to_geojson_form(request)
        except (Zipcodeshapes.DoesNotExist, ValueError):
                return render(request, 'BoxTest.html', {
                        'action':'price_growth_in_bounding_box_to_geojson',
                        'westLongitude': westLongitude,
                        'eastLongitude': eastLongitude,
                        'northLatitude': northLatitude,
                        'southLatitude': southLatitude,
                        'error_message':'There was an error processing your request',
                })
        else:
                context={'data': data_things}
                return render(request, 'GeoJSON.json', context)

def zip_code_test(request):
	context = {}
	return render(request, 'ZipCodeTest.html', context)
	
def geojson_js_parser(request):
	context = {}
	return render(request, 'GeoJSON.js', context)
