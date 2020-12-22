
from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsOverview, name='api-product-overview'),
    path('product-list/', views.productList, name='api-product-list'),
    path('goodandservice/<str:pk>/product-list/', views.goodandserviceProductList, name='api-goodandservice-product-list'),



    path('detail/<str:pk>/', views.productDetail, name='api-product-detail'),
    path('create/', views.productCreate, name='api-product-create'),
    path('update/<str:pk>/', views.productUpdate, name='api-product-update'),
    path('delete/<str:pk>/', views.productDelete, name='api-product-delete'),






]
