from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Article
# Create your views here.
class ArticleList(ListView):
	def get_queryset(self):
		return Article.objects.filter(status=True)
	context_object_name = "articles"
	template_name = "blog/article_list.html"
class ArticleDetail(DetailView):
	def get_object(self):
		return get_object_or_404(Article.objects.filter(status=True),slug=self.kwargs.get("slug"))
	template_name = "blog/article_detail.html"
	context_object_name = "article"
