from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.models import Category
from django.shortcuts import get_list_or_404, get_object_or_404


def apiOverview(request):
    pass
