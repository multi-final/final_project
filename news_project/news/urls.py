from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('',views.index, name = 'index'),
    path('main_ajax/', views.main_ajax, name='main_ajax'),
    path('search/', views.search, name='search'),
    path('introduction/', views.intro, name='intro'),
    path('how/', views.how, name='how'),
]
