from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('welcome',views.welcome,name="welcome"),
    path('main/',views.main, name='main'),
    path('single/',views.single, name='single'),
]