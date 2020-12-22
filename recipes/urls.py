from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='recipes-dashboard'),
    path('<int:pk>/', views.recipe_detail_view, name='recipe-detail'),
    path('create/', views.recipe_create_view, name='recipe-create'),
    path('<int:pk>/delete/', views.recipe_delete_view, name='recipe-delete'),
    path('<str:pk>/update/', views.recipe_update_view, name='recipe-update'),
    path('<str:pk>/remove/', views.remove_wishtocook_view, name='recipe-remove'),

    path('programs/', views.recipe_programs_view, name='programs-list'),


    path('<str:pk>/create-item/', views.createItem, name='recipe-item-create'),
    path('<str:pk>/create-single-item/', views.createSingleItem, name='recipe-single-item-create'),

    path('ajax/load-ings', views.loadIngs, name='ajax-load-ings'),
]
