from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreationForm
from .models import Order, OrderItem


def dashboard(request):
    pendings = Order.objects.filter(status='pe').order_by('-orderDate')
    submitteds = Order.objects.filter(status='su').order_by('-orderDate')
    context = {'object_list': pendings, 'submitteds': submitteds}
    return render(request, 'generalorders/dashboard.html', context)


def order_detail_view(request, pk):
    obj = get_object_or_404(Order, id=pk)
    print(obj)
    pendings = obj.orderitem_set.all()
    context = {'object': obj,
               'pendings': pendings}
    return render(request, 'generalorders/order_detail.html', context)


def order_create_view(request):
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order created successfully ')
            return redirect('generalorders-dashboard')  # TODO
    context = {'form': form}
    return render(request, 'generalorders/order_create.html', context)


def order_submit(request, pk):
    obj = get_object_or_404(Order, id=pk)

    obj.status='su'
    obj.save()
    messages.success(request, f'Order has been Submitted ')
    return redirect('generalorders-dashboard')

