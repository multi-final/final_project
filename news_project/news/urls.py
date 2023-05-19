from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('main_ajax/', views.main_ajax, name='main_ajax'),
    # path('post/', views.post, name = 'post'),
]
