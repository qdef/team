from django.shortcuts import render
from .webscrap import Scores

# Create your views here.

def scores(request):
	#score = Scores.followers(self)
	context={'scores': scores}
	return render(request, 'scores/scores.html', context)