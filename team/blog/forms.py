from django import forms
from .models import BlogArticles

class PostForm(forms.ModelForm):
	class Meta:
		model=BlogArticles
		fields = [
		        "title",
			"sport",
		        "image",
		        "body",
		]