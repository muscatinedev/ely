from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def categoryOverview(request):
    api_urls = {
        'list all categories': '/api/categories/category-list',
        'list food categories': '/api/categories/foodcategory-list',
        'list non food categories': '/api/categories/nonfoodcategory-list',
        'list services categories': '/api/categories/servicecategory-list',
        'category detail  ': '/api/categories/detail/{categoryID}',
        'create new category ': '/api/categories/create',
        'update category ': '/api/categories/update/{categoryID}',
        'delete category ': '/api/categories/delete/{categoryID}',

    }

    return Response(api_urls)


# list all categories
@api_view(['GET'])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# list food categories
@api_view(['GET'])
def foodCategoryList(request):
    categories = Category.objects.filter(type='fd')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# list non food categories
@api_view(['GET'])
def nonfoodCategoryList(request):
    categories = Category.objects.filter(type='nf')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# list food categories
@api_view(['GET'])
def serviceCategoryList(request):
    categories = Category.objects.filter(type='se')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
