from django.urls import path
from . import views

app_name = 'scrap'
urlpatterns = [
    path('', views.scrap, name = 'scrap'),
]
