from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import generic


def overview(request):
    suppliers = Supplier.objects.all().order_by('name')

    context = {'object_list': suppliers}
    return render(request, 'suppliers/overview.html', context)


def supplier_detail_view(request, pk):
    obj = get_object_or_404(Supplier, id=pk)
    context = {'object': obj}
    return render(request, 'suppliers/supplier_detail.html', context)


def supplier_create_view(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Supplier created successfully ')
            return redirect('suppliers-overview')  # TODO
    context = {'form': form}
    return render(request, 'suppliers/supplier_create.html', context)


def supplier_update_view(request, pk):
    instance = get_object_or_404(Supplier, id=pk)
    form = SupplierForm(request.POST or None, instance=instance)
    context = {'object': instance, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, f'Supplier updated successfully ')
        return redirect('suppliers-overview')  # TODO

    return render(request, 'suppliers/supplier_update.html', context)


def supplier_delete_view(request, pk):
    obj = get_object_or_404(Supplier, id=pk)
    context = {'object': obj}
    if request.method == 'POST':
        obj.delete()
        messages.warning(request, f'Supplier has been deleted ')
        return redirect('suppliers-overview')
    return render(request, 'suppliers/supplier_delete.html', context)


class SupplierList(generic.ListView):
    # template_name = 'suppliers/supplier_list.html'

    def get_queryset(self):
        return Supplier.objects.all()

#
# class SupplierDetail(generic.DetailView):
#     template_name = 'suppliers/supplier_detail.html'
#
#     def get_queryset(self):
#         return Supplier.objects.all()
