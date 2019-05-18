from django.urls import path
from . import views

# empty path
# /products
# /products/new/
# /products/1/detail

urlpatterns = [
    path('', views.index),
    path('new/', views.newProducts)
]
