from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoryOverview, name='api-categories-overview'),
    path('category-list/', views.categoryList, name='api-categorys-list'),






]
