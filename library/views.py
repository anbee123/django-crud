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

class Books(APIView):

    def get(self, request):
        #index request
        print(request)
        #get all books from the book table
        books = Book.objects.all()
        #use serializer to format table data to JSON
        data = BookSerializer(book, many=True).data
        return Response(data)
        


    def post(self, request):
        # Post request
        print(request.data)


class BookDetail(APIView):
    def get(self, request):
        #show request
        print(request)
    
    def put(self, request):
        #update request
        print(request)

    def delete(self,request):
        #delete request
        print(request)