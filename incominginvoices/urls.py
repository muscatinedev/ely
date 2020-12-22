
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='incominginvoices-dashboard'),
    path('<int:pk>/', views.incominginvoice_detail_view, name='incominginvoice-detail'),
    path('create/', views.incominginvoice_create_view, name='incominginvoice-create'),
    path('<int:pk>/delete/', views.incominginvoice_delete_view, name='incominginvoice-delete'),
    path('<str:pk>/update/', views.incominginvoice_update_view, name='incominginvoice-update'),




    path('<str:pk>/create-item/', views.createItem, name='incominginvoice-item-create'),
    path('<str:pk>/create-single-item/', views.createSingleItem, name='incominginvoice-single-item-create'),

    path('ajax/load-ings', views.loadGoodAndService, name='ajax-load-goodandserv'),
]
