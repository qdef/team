from django.shortcuts import render

# Create your views here.

def blog(request):
	context={'blog': blog}
	return render(request, 'blog/blog.html', context)