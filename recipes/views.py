from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import RecipeForm, RecipeCreationForm, RecipeUpdateForm, RecipeItemsForm
from .filters import RecipeFilter


def dashboard(request):
    recipes = Recipe.objects.all().order_by('title')
    last5added = Recipe.objects.all().order_by('-date_created')[:5]
    wishToCooks = WishToCookRecipe.objects.all().order_by('-date_created')
    myFilters = RecipeFilter(request.GET, queryset=recipes)
    recipes = myFilters.qs
    context = {'object_list': recipes, 'last5added': last5added, 'wishToCooks': wishToCooks, 'myFilters': myFilters}
    return render(request, 'recipes/dashboard.html', context)


def recipe_create_view(request):
    form = RecipeCreationForm()
    if request.method == 'POST':
        form = RecipeCreationForm(request.POST)
        if form.is_valid():
            saved = form.save()

            cid = saved.id
            messages.success(request, f'Recipe created successfully ')
            return redirect('recipe-update', pk=cid)  # TODO

    context = {'form': form}
    return render(request, 'recipes/recipe_create.html', context)


def recipe_delete_view(request, pk):
    instance = get_object_or_404(Recipe, id=pk)
    context = {'object': instance}
    if request.method == 'POST':
        instance.delete()
        messages.warning(request, f'Recipe deleted successfully ')
        return redirect('recipes-dashboard')

    return render(request, 'recipes/recipe_delete.html', context)


# TODO functoin to add to wishtocook

def remove_wishtocook_view(request, pk):
    instance = get_object_or_404(WishToCookRecipe, id=pk)
    context = {'object': instance}
    if request.method == 'POST':
        instance.delete()
        messages.warning(request, f'Recipe removed successfully ')
        return redirect('recipes-dashboard')

    return render(request, 'recipes/recipe_remove.html', context)


def recipe_update_view(request, pk):
    instance = get_object_or_404(Recipe, id=pk)
    form = RecipeUpdateForm(request.POST or None, instance=instance)
    items = instance.recipeitem_set.all()
    # print('items ', items)
    context = {'object': instance, 'form': form, 'items': items}

    if form.is_valid():
        form.save()
        messages.success(request, f'Recipe updated successfully ')
        return redirect('recipes-dashboard')  # TODO

    return render(request, 'recipes/recipe_update.html', context)


def recipe_detail_view(request, pk):
    obj = get_object_or_404(Recipe, id=pk)
    items = obj.recipeitem_set.all()
    context = {'object': obj, 'items': items}
    return render(request, 'recipes/recipe_detail.html', context)


# TODO non ricalcola i nutritional quando cambia il campo servings !!!!!!!

# def create_item_view(request, pk):
#     # pk of the recipe
#
#
#
#     RecipeItemFormSet = inlineformset_factory(Recipe, RecipeItem, form=RecipeItemsForm)
#
#     recipe = get_object_or_404(Recipe, id=pk)
#
#     formset = RecipeItemFormSet(instance=recipe)
#
#     if request.method == 'POST':
#         formset = RecipeItemFormSet(request.POST, instance=recipe)
#         if formset.is_valid():
#             print('valid')
#             formset.save()
#             return redirect('../')
#         else:
#             print('non valid')
#
#     context = {'formset': formset, 'recipe': recipe}
#
#     return render(request, 'recipes/recipe_ingredient.html', context)


def createItem(request, pk):
    RecipeItemFormSet = inlineformset_factory(Recipe, RecipeItem, fields='__all__')

    recipe = Recipe.objects.get(id=pk)
    # only new items
    # formset = RecipeItemFormSet(queryset=RecipeItem.objects.none(), instance=recipe)
    # formset = RecipeItemFormSet(initial=[{'destination': 'Unknown'}], instance=recipe)
    formset = RecipeItemFormSet(instance=recipe)

    if request.method == 'POST':

        formset = RecipeItemFormSet(request.POST, instance=recipe)
        if formset.is_valid():
            saved = formset.save()

            return redirect('recipe-update', pk=pk)  # TODO

    context = {'formset': formset}
    return render(request, 'recipes/recipe_ing_create.html', context)


def createSingleItem(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeItemsForm(initial={'recipe': recipe})
    if request.method == 'POST':
        form = RecipeItemsForm(request.POST)
        if form.is_valid():
            saved = form.save()
        else:
            print('invalid')
        return redirect('recipe-update', pk=pk)  # TODO

    context = {'form': form}
    return render(request, 'recipes/recipe_single_ing_create.html', context)


def loadIngs(request):
    category_id = request.GET.get('category_id')

    ingres = Ingredient.objects.filter(category=category_id)

    return JsonResponse(list(ingres.values('id', 'name')), safe=False)


def recipe_programs_view(request):
    programs = CookingProgram.objects.all().order_by('name')

    context = {'object_list': programs}
    return render(request, 'recipes/programs.html', context)
