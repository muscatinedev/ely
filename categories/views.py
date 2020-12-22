from django.shortcuts import render, redirect

from .models import Category
from .forms import CategoryForm


# Create your views here.
def overview(request):
    foodcats = Category.objects.filter(type='fd').order_by("name")
    nfcats = Category.objects.filter(type='nf').order_by("name")
    sercats = Category.objects.filter(type='se').order_by("name")
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories-overview')
# pass all cat and append to differenrt div
    context = {'foodcats': foodcats,
               'nfcats': nfcats,
               'sercats': sercats,
               'form': form
               }

    return render(request, 'categories/overview.html', context)
