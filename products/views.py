from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .forms import ProductForm
from .models import Product, Brand
from goodsandservices.models import GoodAndService
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import generic


def overview(request):
    products = Product.objects.all().order_by('name')

    context = {'object_list': products}
    return render(request, 'products/overview.html', context)


def product_detail_view(request, pk):
    obj = get_object_or_404(Product, id=pk)
    context = {'object': obj}
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)

    if form.is_valid():
        gas = request.POST.get('goodOrService')
        print(gas)
        form.fields['goodOrService'].choices = [gas]
        form.save()
        messages.success(request, f'Product created successfully ')
        return redirect('products-overview')  # TODO
    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_update_view(request, pk):
    instance = get_object_or_404(Product, id=pk)
    form = ProductForm(request.POST or None, instance=instance)
    context = {'object': instance, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, f'Product updated successfully ')
        return redirect('products-overview')  # TODO

    return render(request, 'products/product_update.html', context)


def product_delete_view(request, pk):
    obj = get_object_or_404(Product, id=pk)
    context = {'object': obj}
    if request.method == 'POST':
        obj.delete()
        messages.warning(request, f'Product has been deleted ')
        return redirect('products-overview')
    return render(request, 'products/product_delete.html', context)


def loadGas(request):
    category_id = request.GET.get('category_id')
    print(category_id)
    goodsandservices = GoodAndService.objects.filter(category=category_id)

    return JsonResponse(list(goodsandservices.values('id', 'name')), safe=False)
