from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredientOverview, name='api-ingredients-overview'),
    path('ingredient-list/', views.ingredientList, name='api-ingredients-list'),
    path('category/<str:pk>/ingredient-list/', views.categoryIngredientList, name='api-category-ingredients-list'),
    path('no-nutritionals-ingredient-list/', views.noNutritionalIngredientList, name='api-no-nutr-ingredients-list'),
    path('caloriesgenerated/<str:pk>/', views.caloriesGenerated, name='api-ingredient-cal-generated'),





]
