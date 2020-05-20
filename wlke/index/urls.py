from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('jumbo/<int:jumbo_id>/', views.jumbo_detail, name="jumbodetail"),
]
