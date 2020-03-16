from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('user', views.user_panel, name='user_panel'),
]