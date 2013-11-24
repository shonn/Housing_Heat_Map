from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('HeatMap.views',
	url(r'^getHousingGrowthinBoundingbox.json$', 'price_growth_in_bounding_box_to_geojson', name ='price_growth_in_bounding_box_to_geojson'),
	url(r'^getHousingGrowthinBoundingboxTestForm.html$','price_growth_in_bounding_box_to_geojson_form'),
	url(r'^ZipCodeTest.html$', 'zip_code_test'),
	url(r'^GeoJSON.js$','geojson_js_parser'),
    url(r'^(?P<housezip>\d{5})/$', 'home')
#    url(r'', 'home'),
) 


#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'framework.views.home', name='home'),
    # url(r'^framework/', include('framework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
