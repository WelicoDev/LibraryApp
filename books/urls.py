from django.urls import path
from .views import BookListApi, BookDetailApi, BookDeleteApi, BookUpdateApi, BookCreateApi, BookListCreateApi, BookEditApi

urlpatterns = [
    path('books/', BookListApi.as_view(), name="books_list"),
    path('books/create/', BookCreateApi.as_view(), name="books_create"),
    path('books/<int:pk>/', BookDetailApi.as_view(), name="books_detail"),
    path('books/<int:pk>/delete/', BookDeleteApi.as_view(), name="books_delete"),
    path('books/<int:pk>/update', BookUpdateApi.as_view(), name="books_edit"),
    path('books/list/create/', BookListCreateApi.as_view(), name="books_list_create"),
    path('books/<int:pk>/edit/', BookEditApi.as_view(), name="books_edit"),
]