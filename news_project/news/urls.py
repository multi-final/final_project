from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.main, name = 'main'),
    # path('post/', views.post, name = 'post'),
]
