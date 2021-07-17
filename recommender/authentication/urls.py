from django.urls import path
from . import views

urlpatterns = [
    path('login-page', views.login_page),
    path('login', views.user_login),
    path('logout', views.user_logout)
]