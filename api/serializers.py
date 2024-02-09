from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class AuthorSerialiser(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ['id',"username","first_name","last_name"]
class ArticleSerialiser(serializers.ModelSerializer):
	author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
	class Meta:
		model = Article
		fields = "__all__"
	
class UserSerialiser(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"