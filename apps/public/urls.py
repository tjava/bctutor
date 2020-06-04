from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),

]