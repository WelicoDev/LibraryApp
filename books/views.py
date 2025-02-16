# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets


# Create your views here.

class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status":f"Returned {len(books)} books",
            "books":serializer_data
        }

        return Response(data)

# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApi(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status": "Successfully",
                "book": serializer_data
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,
                             "message":"Book is not found"}, status=status.HTTP_404_NOT_FOUND)



# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApi(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()

            return Response({
                "status":True,
                "message":"Successfully deleted"
            }, status=status.HTTP_200_OK)

        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                }, status=status.HTTP_400_BAD_REQUEST
            )

# class BookUpdateApi(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApi(APIView):
    def put(self, request, pk):
        books = Book.objects.all()
        book = get_object_or_404(books, id=pk)
        data = request.data
        serializer_data = BookSerializer(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
            book_saved = serializer_data.save()

        return Response(
                {
                    "status":True,
                    "message":f"Book {book_saved} successfully updated"
                }, status=status.HTTP_200_OK
            )



# class BookCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApi(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status":f"Books are saved to the database",
                "books":data
            }
            return Response(data)
class BookListCreateApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#
#     return Response(serializer.data)
