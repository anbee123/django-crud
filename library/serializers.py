#think of serializers as middleware that formats your DB data into something the browser can read
from rest_framework import serializers
from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'