from django.urls import path
from .views import Books, BookDetail

urlpatterns = [
    path('', Books.as_view(), name='books'),
]