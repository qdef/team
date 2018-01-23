from django.db import models
from django.core.urlresolvers import reverse

class BlogArticles(models.Model):
	FOOTBALL = 'Football'
	RUGBY = 'Rugby'
	AMERICAN = 'American Football'
	SPORTS_CHOICES = (
	    (FOOTBALL, 'Football'),
            (RUGBY, 'Rugby'),
            (AMERICAN, 'American Football'),
	    )
	title = models.CharField(max_length=200)
	sport = models.CharField(choices=SPORTS_CHOICES, max_length=20)
	body = models.TextField()
	image = models.FileField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/blog/detail/%s/" %(self.pk)


