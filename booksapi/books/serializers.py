# Import the Book model
# Import the REST Framework serializer
# Create a new class that links the Book with its serializer

from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        # fields = ('name', 'alias') # use all the fields
        fields = ['name', 'author', 'rating', 'reviews', 'price', 'year', 'genre']


    # name = models.CharField(max_length=256)
    # author = models.CharField(max_length=128)
    # rating = models.FloatField(default=0)
    # reviews = models.IntegerField(default=0)
    # price = models.IntegerField(default=0)
    # year = models.CharField(max_length=8)
    # genre = models.CharField(max_length=32)