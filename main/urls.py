from django.urls import path
from .views import index, about, feedback, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
]
