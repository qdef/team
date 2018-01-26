from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogArticles


# Create your views here.

def index(request):
	return render(request, '../templates/home/index.html')

def contact(request):
	return render(request, '../templates/home/contact.html')

def liste_index(request):
	articles_list = BlogArticles.objects.all().order_by("-created")[:10]
	context = { 'blog_articles': articles_list}
	return render(request, '../templates/home/index.html', context)

