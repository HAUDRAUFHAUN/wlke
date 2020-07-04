from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="storage_index"),
    path('delete/<int:file_id>/', views.delete),
]
