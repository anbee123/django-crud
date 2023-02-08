from rest_framework.views imort APIView
from rest_framework import Response
from rest_framework import status
from .serializers import Bookserializer
from .models import Book

# Create your views here.

# def index(request):
#     books = Book.objects.all()
#     data = list(books.values())
#     return JsonResponse(data, safe=False)

# class /books
# GET /books -index
# POST /books - create

#class /book/:id
# GET /books/:id - show
# PUT /books/:id - update
# DELETE /books/:id - delete