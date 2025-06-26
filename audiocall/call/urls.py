# call/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-token/', views.get_token, name='get_token'),
]