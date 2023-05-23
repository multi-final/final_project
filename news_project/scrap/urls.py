from django.urls import path
from . import views

app_name = 'scrap'
urlpatterns = [
    path('', views.scrap, name = 'scrap'),
    path('insert/<int:id>', views.scrap_insert),
    path('delete/<int:id>', views.scrap_delete),
]
