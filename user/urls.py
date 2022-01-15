from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.user, name='user'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('user_profile', views.getUser, name='userDetails'),
    path('fav', views.getFavorite, name='fav')
]
