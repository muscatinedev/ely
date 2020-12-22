
from django.urls import path, include

urlpatterns = [
    path('products/', include('api.products.urls')),
    path('ingredients/', include('api.ingredients.urls')),
    path('categories/', include('api.categories.urls')),






    ]
