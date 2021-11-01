from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('', views.product, name='product'),
    path('product/<int:id>/', views.product_detail, name = "product_detail")
]