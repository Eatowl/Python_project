from django.db import models
from django.utils import timezone
# Create your models here.

class article(models.Model):
	article_title = models.CharField(max_length=200)	
	article_text = models.TextField()
	article_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.article_title
	
class comment(models.Model):
	comment_name = models.CharField(max_length=100)
	comment_text = models.TextField()
	comment_data = models.DateTimeField(auto_now_add=True)
	comment_article = models.ForeignKey(article)
	def __str__(self):
		return self.comment_name



