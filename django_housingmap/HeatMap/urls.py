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
<<<<<<< HEAD
        url(r'', 'home')
=======
	url(r'^Chart/$', 'home')
#    url(r'', 'home'),
>>>>>>> c0607889fa072addb802d1ed60e33f4d403a5592
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
