from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book


# ModelViewSet is a special view that Django Rest Framework provides.
# It will handle GET and POST for Books without us having to do any more work.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
