from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('edit/<int:note_id>/', views.edit),
    path('archived/', views.archived),
    path('archive/<int:note_id>/', views.archive),
    path('dearchive/<int:note_id>/', views.dearchive),
    path('delete/<int:note_id>/', views.delete),
]
