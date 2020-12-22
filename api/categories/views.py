from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def categoryOverview(request):
    api_urls = {
        'list all categories': '/api/categories/category-list',

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
