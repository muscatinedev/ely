from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.overview, name='products-overview'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('create/', views.product_create_view, name='product-create'),
    path('<int:pk>/update/', views.product_update_view, name='product-update'),
    path('<int:pk>/delete/', views.product_delete_view, name='product-delete'),

    path('ajax/load-gas', views.loadGas, name='ajax-load-gas')
    ]
