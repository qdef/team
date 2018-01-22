from django.shortcuts import render

# Create your views here.

def scores(request):
	context={'scores': scores}
	return render(request, 'scores/scores.html', context)