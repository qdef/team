from rest_framework import serializers
from .models import BlogArticles
from django.contrib.auth.models import User



class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogArticles
        fields = ('title', 'body', 'sport', 'created', 'updated', 'image')
		
class USerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'date_joined', 'last_login')
