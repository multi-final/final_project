from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
