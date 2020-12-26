from django.urls import path
from . import views

urlpatterns = [
    path('', views.incominginvoicesOverview, name='api-incominginvoices-overview'),
    path('incominginvoices-list/', views.incominginvoiceList, name='api-incominginvoices-list'),






]
