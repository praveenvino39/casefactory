from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_order),
    path('create/', views.create_order),
    path('<int:id>', views.get_orderby_id),
]
