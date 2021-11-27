from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.user, name='user'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('<int:id>', views.getUser, name='userDetails')
]
