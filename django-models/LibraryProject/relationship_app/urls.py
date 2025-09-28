from django.urls import path
from . import views
from .views import book_list

urlpatterns = [
    path('books/', views.book_list, name="book_list"),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name="library_detail"),
]