from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='ingredients-overview'),
    path('ingredient/<int:pk>/', views.ingredient_detail_view, name='ingredient-detail'),
    path('ingredient/create/', views.ingredient_create_view, name='ingredient-create'),
    path('ingredient/<int:pk>/update/', views.ingredient_update_view, name='ingredient-update'),
    path('ingredient/<int:pk>/delete/', views.ingredient_delete_view, name='ingredient-delete'),
    path('nonut/', views.showIngredientsNoNutritrional, name='ingredient-nonut'),
    # path('nonuthundred/', views.inghun, name='ingredient-hund'),
]
