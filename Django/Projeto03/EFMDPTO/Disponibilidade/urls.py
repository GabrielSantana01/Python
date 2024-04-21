from django.urls import path
from Disponibilidade.views import index
urlpatterns = [
    path('', index, name='index'),
]