from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    data = list(books.values())
    return JsonResponse(data, safe=False)