from django.forms import ModelForm
from models import comment, article

class CommentForm(ModelForm):
	class Meta:
		model = comment
		fields = ('comment_name', 'comment_text')

class ArticleForm(ModelForm):
	class Meta:
		model = article
		fields = ('article_title', 'article_text') 
