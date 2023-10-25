from django.urls import path
from .views import index, about, feedback, contact, book, book_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
    path('book/', book, name='book'),
    path('book/<int:pk>/', book_detail, name='book-detail'),
]
