from django.urls import path
from . import views

app_name="catalog"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
