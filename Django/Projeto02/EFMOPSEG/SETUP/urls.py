from django.contrib import admin
from django.urls import path
from SETUP.login import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('inicial', views.inicial, name='inicial'),
]
