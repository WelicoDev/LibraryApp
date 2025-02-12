from rest_framework import serializers
from django.utils.html import strip_tags
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'body', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphabet chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Iltimos kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )
        # check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz!"
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notog'ri kiritilgan !"
                }
            )

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(max_length=255)
#     body = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=250)
#     isbn = serializers.IntegerField()
#     price = serializers.IntegerField()