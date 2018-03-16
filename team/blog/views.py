from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogArticles
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from rest_framework import viewsets
from .serializers import BlogSerializer, USerSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = BlogArticles.objects.all()
    serializer_class = BlogSerializer

class USerViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = User.objects.all()
    serializer_class = USerSerializer



def liste(request):
	articles_list = BlogArticles.objects.all().order_by("-created")[:10]
	context = { 'blog_articles': articles_list}
	return render(request, 'blog/list.html', context)


def football(request):
	football_list = BlogArticles.objects.filter(sport='Football').order_by("-created")
	context = { 'blog_articles': football_list}
	return render(request, 'blog/football.html', context)

def rugby(request):
	rugby_list = BlogArticles.objects.filter(sport='Rugby').order_by("-created")
	context = { 'blog_articles': rugby_list}
	return render(request, 'blog/rugby.html', context)

def american(request):
	american_list = BlogArticles.objects.filter(sport='American Football').order_by("-created")
	context = { 'blog_articles': american_list}
	return render(request, 'blog/american.html', context)

def detail(request, pk):
	articles = BlogArticles.objects.get(pk=pk)
	articles_list = BlogArticles.objects.filter(sport=articles.sport).order_by("-created")[:10]
	context = { 'full_article': articles, 'blog_articles': articles_list}
	return render(request, 'blog/detail.html', context)

@login_required
def create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.author=request.user
		instance.save()
		#messages.success(request, "Post was successfully created!")
		return redirect('detail', pk=instance.get_pk())
	else:
		#messages.success(request, "Post creation failed.")
		context={"form":form}
	return render(request, "blog/post_form.html",context)

@login_required
def edit(request, pk=None):
	instance = get_object_or_404(BlogArticles, pk=pk)
	form=PostForm(request.POST or None, request.FILES or None, instance=instance)
	if request.user==instance.author:
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			#messages.success(request, "Post was successfully updated!")
			return redirect('detail', pk=pk)
		else:
			pass
	else:
		return redirect('user_error')	
		#messages.success(request, "Post modification failed.")
	context={"title":instance.title, "instance":instance, "form":form}
	return render(request, "blog/edit_form.html", context)


def delete(request, pk=None):
	instance=get_object_or_404(BlogArticles, pk=pk)
	if request.user==instance.author:
		instance.delete()
		#messages.success(request, "Post was successfully deleted.")
		return redirect('blog')
	else:
		return redirect('user_error')

def user_error(request):
	return render(request, "blog/user_error.html")
	


