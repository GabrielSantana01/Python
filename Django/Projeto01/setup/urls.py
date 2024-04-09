from django.urls import path
from Django import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('inicial', views.inicial, name='inicial'),

]
