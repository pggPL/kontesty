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
    path('problems', views.problems, name='problems'),
    path('user_file', views.user_file, name='user_file'),
    path('check_panel', views.check_panel, name='check_panel'),
    path('update_check', views.update_check, name='update_check'),
    path('change_check', views.change_check, name='change_check'),
    path('solutions_check', views.solutions_check, name='solutions_check'),
    path('display_image_check', views.display_image_check, name='display_image_check'),
    path('remove', views.remove, name='remove')
]