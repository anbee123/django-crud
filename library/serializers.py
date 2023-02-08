#think of serializers as middleware that formats your DB data into something the browser can read
from rest_framework import serializers
from .models.book import book 

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Bookserializer
        fields = '__all__'