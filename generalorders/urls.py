from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='generalorders-dashboard'),
    path('<int:pk>/', views.order_detail_view, name='generalorder-detail'),
    path('create/', views.order_create_view, name='generalorder-create'),
# submit order
    path('<int:pk>/submit_order', views.order_submit, name='generalorder-submit'),

]
