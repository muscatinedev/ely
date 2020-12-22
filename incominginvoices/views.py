from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .filters import InvoiceFilter


def dashboard(request):
    invoices = Invoice.objects.all().order_by('invoiceDate')
    last5added = Invoice.objects.all().order_by('-registrationDate')[:5]
    myFilters = InvoiceFilter(request.GET, queryset=invoices)
    recipes = myFilters.qs
    context = {'object_list': recipes, 'last5added': last5added, 'myFilters': myFilters}
    return render(request, 'incominginvoices/dashboard.html', context)


def incominginvoice_detail_view(request):
    pass


def incominginvoice_create_view(request):
    pass


def incominginvoice_delete_view(request, pk):
    pass


def incominginvoice_update_view(request, pk):
    pass


def createItem(request, pk):
    pass


def createSingleItem(request, pk):
    pass


def loadGoodAndService(request):
    pass
