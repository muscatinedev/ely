from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoryOverview, name='api-categories-overview'),
    path('category-list/', views.categoryList, name='api-categorys-list'),
    path('foodcategory-list/', views.foodCategoryList, name='api-foodcategorys-list'),
    path('nonfoodcategory-list/', views.nonfoodCategoryList, name='api-nonfoodcategorys-list'),
    path('servicecategory-list/', views.serviceCategoryList, name='api-servicecategorys-list'),



]
