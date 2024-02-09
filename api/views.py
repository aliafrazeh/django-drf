from django.shortcuts import render
from blog.models import Article
from rest_framework.permissions import IsAdminUser
from .serializers import ArticleSerialiser,UserSerialiser,AuthorSerialiser
from .permissions import IsSuperUser,IsStaffOrReadOnly,IsOwnerOrReadOnly,IsSuperUserOrStaffReadOnly
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.
class ArticleViewSet(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser
	filterset_fields = ['status','author__username','author__first_name']
	ordering_fields = ['publish','status']
	ordering = ['-publish']
	search_fields = ['title','content','author__username','author__first_name','author__last_name']
	def get_permissions(self):
		if self.action in ['list','create']:
			permission_classes = [IsStaffOrReadOnly]
		else:
			permission_classes = [IsStaffOrReadOnly,IsAuthenticatedOrReadOnly]
		return [permission() for permission in permission_classes]
# class ArticleList(ListCreateAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerialiser

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerialiser
# 	lookup_field ="slug"
# 	permission_classes = (IsStaffOrReadOnly,IsOwnerOrReadOnly)
# class UserList(ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerialiser
# 	permission_classes = (IsSuperUserOrStaffReadOnly,)

# class UserDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerialiser
# 	permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerialiser
	permission_classes = (IsSuperUserOrStaffReadOnly,)


class AuthorRetrieve(RetrieveAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = AuthorSerialiser