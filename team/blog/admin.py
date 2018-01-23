from django.contrib import admin
from .models import BlogArticles

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ["id", "title", "created", "sport"]
	list_display_links = ["title"]
	list_filter = ["sport"]
	search_fields = ["title", "body"]
	class Meta:
		model = BlogArticles

admin.site.register(BlogArticles, BlogAdmin)