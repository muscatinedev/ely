from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from goodsandservices.models import GoodAndService
from products.models import Product


@api_view(['GET'])
def productsOverview(request):
    api_urls = {
        'list all products': '/api/products/product-list',
        'list  products of a particular goodandservice': '/api/products/goodandservice/{goodandserviceId}/product-list',
        'product detail  ': '/api/products/detail/{productID}',
        'create new product ': '/api/products/create',
        'update product ': '/api/products/update/{productID}',
        'delete product ': '/api/products/delete/{productID}',


    }
    return Response(api_urls)


# list all products
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# list  products of goodandservice
@api_view(['GET'])
def goodandserviceProductList(request, pk):
    goodandservice = GoodAndService.objects.get(id=pk)
    products = Product.objects.filter(goodOrService=goodandservice)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



# detail of a product
@api_view(['GET'])
def productDetail(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def productUpdate(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()

    return Response('deleted')

#
# @api_view(['GET'])
# def productofgoodandservicesList(request, gasid):
#     fgas = get_object_or_404(GoodAndService, id=gasid)
#     prods = Product.objects.filter(goodOrService=fgas)
#     serializer = ProductSerializer(prods, many=True)
#     return Response(serializer.data)
