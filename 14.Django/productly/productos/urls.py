from django.urls import path
from . import views

# /productos
urlpatterns = [
    path('', views.index, name='index')
]
