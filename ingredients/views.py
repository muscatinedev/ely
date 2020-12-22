import time
from django.shortcuts import render, redirect
from .models import Ingredient
from .forms import IngredientForm, IngredientUpdateForm
from .filters import IngredientFilter
from django.shortcuts import get_object_or_404
from django.contrib import messages


def overview(request):
    ingredients = Ingredient.objects.all().order_by('name')

    myFilter = IngredientFilter(request.GET, queryset=ingredients)
    ingredients = myFilter.qs
    context = {'myFilter': myFilter, 'object_list': ingredients}
    return render(request, 'ingredients/overview.html', context)



def showIngredientsNoNutritrional(request):
    ingredients = Ingredient.objects.filter(cal=0).order_by('category')
    context = {'object_list': ingredients}
    return render(request, 'ingredients/nonut.html', context)









def ingredient_detail_view(request, pk):
    obj = get_object_or_404(Ingredient, id=pk)
    context = {'object': obj}
    return render(request, 'ingredients/ingredient_detail.html', context)


def ingredient_create_view(request):
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ingredient created successfully ')
            return redirect('ingredients-overview')  # TODO
    context = {'form': form}
    return render(request, 'ingredients/ingredient_create.html', context)


def ingredient_update_view(request, pk):
    instance = get_object_or_404(Ingredient, id=pk)
    form = IngredientUpdateForm(request.POST or None, instance=instance)
    context = {'object': instance, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, f'Ingredient updated successfully ')
        return redirect('ingredients-overview')  # TODO

    return render(request, 'ingredients/ingredient_update.html', context)


def ingredient_delete_view(request, pk):
    obj = get_object_or_404(Ingredient, id=pk)
    context = {'object': obj}
    if request.method == 'POST':
        obj.delete()
        messages.warning(request, f'Ingredient has been deleted ')
        return redirect('ingredients-overview')
    return render(request, 'ingredients/ingredient_delete.html', context)


def inghun(request):
    ingredients = Ingredient.objects.all()
    for ing in ingredients:
        cal = ing.cal*100
        car = ing.car*100
        pro = ing.pro*100
        fat = ing.fat*100
        sta = ing.sta*100

        ing.cal = cal
        ing.car = car
        ing.pro = pro
        ing.fat = fat
        ing.sta = sta
        ing.save()

        print(ing, 'Updated')
        time.sleep(0.3)
    return redirect('/')
