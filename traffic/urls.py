from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import *
from intersections.views import* 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', homepage, name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^intersections/$', 'intersections.views.intersections'),
	url(r'^intersections/', intersections, name='intersections'),
	url(r'^login/', login_user, name='login'),
	url(r'^devices/', devices, name='devices'),
	url(r'^roads/', roads, name = 'roads'),
	url(r'^accidents/', accidents, name='accidents'),
	url(r'^addAccident/', newAccident, name='addAccident'),
	url(r'^addDevice/', newDevice, name='addDevice'),
	url(r'^addIntersection/', newIntersection, name='addIntersection'),
	url(r'^addRoad/', newRoad, name='addRoad'),
	#url(r'^pages/', include('django.contrib.flatpages.urls')),
)
