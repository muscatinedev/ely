from django.shortcuts import render
from .models import Allergen
from .forms import AllergenForm


# Create your views here.
def overview(request):
    allergens = Allergen.objects.all().order_by("name")
    form = AllergenForm()
    context = {'allergens': allergens,
               'form': form
               }

    return render(request, 'allergens/overview.html', context)
