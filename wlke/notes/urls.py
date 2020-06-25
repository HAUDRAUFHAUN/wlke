from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<int:note_id>/', views.edit),
    path('delete/<int:note_id>/', views.delete),
]
