from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', include('HeatMap.urls', namespace = 'HeatMap')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'framework.views.home', name='home'),
    # url(r'^framework/', include('framework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
