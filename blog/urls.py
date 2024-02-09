from django.urls import path
from .views import ArticleList,ArticleDetail
from rest_framework.authtoken.views import obtain_auth_token
app_name = "blog"

urlpatterns = [
    path("",ArticleList.as_view(),name="list"),
    path("<slug:slug>",ArticleDetail.as_view(),name="detail"),
    path('api-token-auth/',obtain_auth_token)
]
