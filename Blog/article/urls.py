from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/', 'article.views.output'),
    url(r'^2/', 'article.views.templates'),
    url(r'^3/', 'article.views.template_simple'),
    url(r'^article/all/$', 'article.views.personal_blog'),
    url(r'^article/get/(?P<article_id>\d+)/$', 'article.views.Article'),
    url(r'^article/addcomment/(?P<post_id>\d+)/$', 'article.view.addcomment'),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^article/addarticle/$', 'article.views.addarticle'),


    url(r'^$', 'article.views.personal_blog'),
	#url(r'^article/get/(?<article_id>)\d+/$', 'article.views.article'),
)
