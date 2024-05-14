from django.urls import path
from request.views import index

urlpatterns = (
    path('', index,name='index'),
)