from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^intersections/$', 'intersections.views.intersections'),
	url(r'^login/$', 'intersections.views.login_user'),
	url(r'^devices/$', 'intersections.views.devices'),
	url(r'^roads/$', 'intersections.views.roads'),
	url(r'^accidents/$', 'intersections.views.accidents'),
	
)
