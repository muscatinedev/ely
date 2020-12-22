from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('supplier/', views.overview, name='suppliers-overview'),
    path('supplier/<int:pk>/', views.supplier_detail_view, name='supplier-detail'),
    path('supplier/create/', views.supplier_create_view, name='supplier-create'),
    path('supplier/<int:pk>/update/', views.supplier_update_view, name='supplier-update'),
    path('supplier/<int:pk>/delete/', views.supplier_delete_view, name='supplier-delete'),

]
