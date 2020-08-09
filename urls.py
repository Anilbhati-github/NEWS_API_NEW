from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsList.as_view()),
    path('create/', views.create_models),
    path('Login/', views.LoginList.as_view()),
    path('Category/', views.CategoryList.as_view()),
    path('NewsMaster/', views.NewsMasterList.as_view()),
    path('UserData/', views.UserDataList.as_view()),
    path('User/', views.UserList.as_view()),
    ]