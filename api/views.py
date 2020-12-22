from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import (CategorySerializer,
                          GoodAndServiceSerializer,
                          PersonnelSerializer,
                          ProductSerializer,
                          BrandSerializer,
                          AllergenSerializer,

                          )

from allergens.models import Allergen
from categories.models import Category
from django.shortcuts import get_list_or_404, get_object_or_404
from goodsandservices.models import GoodAndService
from personnels.models import *
from products.models import Product, Brand


#
# @api_view(['GET'])
# def categoriesApiOverview(request):
#
#     api_urls = {
#         'list': '/category/',
#         'list_food': '/category/food/',
#         'list_nonfood': '/category/nonfood/',
#         'list_services': '/category/servicies/',
#         'detail view': '/category/<int:pk>/',
#         'create': '/category/create/',
#         'update': '/category/<int:pk>/update/',
#         'delete': '/category/<int:pk>/delete/',
#
#
#     }
#     return Response(api_urls)
#
#
# # 'list': '/category/',
# @api_view(['GET'])
# def categoryList(request):
#     categories = Category.objects.all().order_by("name")
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
#
# # 'list_food': '/category/food/',
# @api_view(['GET'])
# def foodCategoryList(request):
#     categories = Category.objects.filter(type='fd').order_by("name")
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
#
# # 'list_nonfood': '/category/nonfood/',
# @api_view(['GET'])
# def nonFoodCategoryList(request):
#     categories = Category.objects.filter(type='nf').order_by("name")
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
#

# # DETAIL
# @api_view(['GET'])
# def categoryDetail(request, pk):
#     category = get_object_or_404(Category, id=pk)
#     serializer = CategorySerializer(category, many=False)
#     return Response(serializer.data)
#
#
#
#
# # create
# @api_view(['POST'])
# def categoryCreate(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def categoryUpdate(request, pk):
#     category = get_object_or_404(Category, id=pk)
#     serializer = CategorySerializer(instance=category, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def categoryDelete(request, pk):
#     category = get_object_or_404(Category, id=pk)
#     category.delete()
#
#     return Response('Item deleted!')
#
#
# # ----------------------- GOOD AND SERVICE -------------------------
#
# @api_view(['GET'])
# def goodandsevicesApiOverview(request):
#
#     api_urls = {
#         'list': '/goodandservice/',
#
#         'detail view': '/goodandservice/<int:pk>/',
#         'create': '/goodandservice/create/',
#         'update': '/goodandservice/<int:pk>/update/',
#         'delete': '/goodandservice/<int:pk>/delete/',
#
#
#     }
#     return Response(api_urls)


@api_view(['GET'])
def goodandservicesofcatList(request, catid):
    fcategory = get_object_or_404(Category, id=catid)
    gas = GoodAndService.objects.filter(category=fcategory)
    serializer = GoodAndServiceSerializer(gas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productofgoodandservicesList(request, gasid):
    fgas = get_object_or_404(GoodAndService, id=gasid)
    prods = Product.objects.filter(goodOrService=fgas)
    serializer = ProductSerializer(prods, many=True)
    return Response(serializer.data)



class GoodandserviceView(viewsets.ModelViewSet):
    queryset = GoodAndService.objects.all()
    serializer_class = GoodAndServiceSerializer


class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodCategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.filter(type='fd')
    serializer_class = CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class AllergenView(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
