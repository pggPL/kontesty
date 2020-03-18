from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('user', views.user_panel, name='user_panel'),
    path('register', views.register, name='register'),
    path('rules', views.rules, name='rules'),
    path('user_settings', views.user_settings, name='user_settings'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('change_password', views.change_password, name='change_password'),
    path('problems', views.problems, name='problems')
]