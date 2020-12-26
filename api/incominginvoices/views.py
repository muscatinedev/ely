from rest_framework.decorators import api_view
from rest_framework.response import Response
from incominginvoices.models import Invoice, InvoiceItem
from api.incominginvoices.serializers import IncominginvoiceSerializer


@api_view(['GET'])
def incominginvoicesOverview(request):
    api_urls = {
        'list all invoices': '/api/incominginvoices/incominginvoices-list',


    }

    return Response(api_urls)


# list all invoices
@api_view(['GET'])
def incominginvoiceList(request):
    invoices = Invoice.objects.all()
    serializer = IncominginvoiceSerializer(invoices, many=True)
    return Response(serializer.data)


