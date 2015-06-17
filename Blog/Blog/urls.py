from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   	url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('article.urls')),
	url(r'^basicview/', include('article.urls')),
	url(r'^auth/', include('login.urls')),
	url(r'^', include('article.urls')),

)
