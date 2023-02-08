from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import get_objetc_or_404

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

class Books(APIView):

    def get(self, request):
        #index request
        print(request)
        #get all books from the book table
        books = Book.objects.all()
        #use serializer to format table data to JSON
        data = BookSerializer(books, many=True).data
        return Response(data)



    def post(self, request):
        # Post request
        print(request.data)
        #format data for postgres
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, pk):
        #show request
        print(request)
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)

    
    def put(self, request, pk):
        #update request
        print(request)

    def delete(self,request, pk):
        #delete request
        print(request)