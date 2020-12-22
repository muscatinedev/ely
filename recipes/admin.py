from django.contrib import admin
from .models import *

admin.site.register(Recipe)
admin.site.register(RecipeItem)
admin.site.register(RecipeLine)
admin.site.register(RecipeLineItem)
admin.site.register(CookingProgram)
admin.site.register(CookingProgramPhase)
