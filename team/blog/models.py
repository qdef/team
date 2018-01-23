from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=200)
	sport = models.CharField(   )
	body = models.TextField()
	image = models.FileField(null=True, blank=True)
	date = models.DateTimeField()
	
	def __str__(self):
		return self.title
	
#	def get_absolute_url(self):
#		return reverse("detail", kwargs={"id":self.id})
#		#return "/blog/%s/" %(self.id)
	

