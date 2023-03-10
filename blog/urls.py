from django.urls import path
from .views import index, card

urlpatterns=[
    path('', index, name='index'),
    path('', card, name='card'),
    
]