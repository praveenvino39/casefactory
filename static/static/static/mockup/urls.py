from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('models', views.model_list),
    path('brands', views.get_brands),
    path('models/<int:id>', views.get_model_by_id),
    path('model/<int:id>', views.get_model_from_qikink),
    path('get_models/<int:id>', views.get_model_list),

]
