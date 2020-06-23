from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/', views.edit),
    path('view/', views.view),
]
