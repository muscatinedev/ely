from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import InvoiceCreationForm
from .models import *
from .filters import InvoiceFilter


def dashboard(request):
    invoices = Invoice.objects.all().order_by('invoiceDate')
    last5added = Invoice.objects.all().order_by('-registrationDate')[:5]
    myFilters = InvoiceFilter(request.GET, queryset=invoices)
    recipes = myFilters.qs
    context = {'object_list': recipes, 'last5added': last5added, 'myFilters': myFilters}
    return render(request, 'incominginvoices/dashboard.html', context)


def incominginvoice_detail_view(request, pk):
    pass


def incominginvoice_create_view(request):
    form = InvoiceCreationForm()
    if request.method == 'POST':
        form = InvoiceCreationForm(request.POST)
        if form.is_valid():
            saved = form.save()
            cid = saved.id
            messages.success(request, f'Invoice created successfully ')

            return redirect('incominginvoices-dashboard')

            # return redirect('recipe-update', pk=cid)  # TODO

    context = {'form': form}
    return render(request, 'incominginvoices/incominginvoice_create.html', context)


def incominginvoice_delete_view(request, pk):
    instance = get_object_or_404(Invoice, id=pk)
    context = {'object': instance}
    if request.method == 'POST':
        instance.delete()
        messages.warning(request, f'Invoice deleted successfully ')
        return redirect('incominginvoices-dashboard')

    return render(request, 'incominginvoices/incominginvoice_delete.html', context)


def incominginvoice_update_view(request, pk):
    pass


def createItem(request, pk):
    pass


def createSingleItem(request, pk):
    pass


def loadGoodAndService(request):
    pass
