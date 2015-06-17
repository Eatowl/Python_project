from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^login/$', 'login.views.login'),
    url(r'^logout/$', 'login.views.logout'),
    url(r'^register/$', 'login.views.register'),
	
)
