from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('legal', views.legal_notice, name='legal')
]
