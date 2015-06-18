from article.models import article, comment
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from forms import CommentForm, ArticleForm
from django.core.exceptions import ObjectDoesNotExist 
from django.core.context_processors import csrf
from django.contrib import auth 
from django.views.decorators.csrf import csrf_exempt
import simplejson

# Create your views here.
def output(request):
	view = "Output"
	html = "<html><body>This is %s view</body></html>" % view
	return HttpResponse(html)

def templates(request):
	view = "templates"
	temp = get_template('base.html')
	html = temp.render(Context({'name': view}))
	return HttpResponse(html)

def template_simple(request):
	view = "template_simple"
	return render_to_response('base.html', {'name': view})

def personal_blog(request):
	return render_to_response('personal_blog.html', {'articles': article.objects.all(), 'username': auth.get_user(request).username})

def Article(request, article_id=1):
	comment_form = CommentForm
	slov = {}
	slov['Article'] = article.objects.get(id = article_id)
	slov['comment'] = comment.objects.filter(comment_article_id=article_id)
	slov['form'] = comment_form
	slov['username'] = auth.get_user(request).username
	slov.update(csrf(request))
	return render_to_response('article.html', slov)

def addcomment(request, article_id):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			Comment = form.save(commit=False)
			Comment.comment_article = article.objects.get(id = article_id)
			form.save()
	return redirect('/article/get/%s/' % article_id)

def addarticle(request):
	if request.POST:
		form2 = ArticleForm(request.POST)
		if form2.is_valid():
			form2.save()
		return render_to_response('addarticle.html')

