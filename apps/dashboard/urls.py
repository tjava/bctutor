from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('shareprofile', views.shareprofile, name='shareprofile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('becomeinstructor', views.becomeinstructor, name='becomeinstructor'),
    path('newcourse', views.newcourse, name='newcourse'),
    path('allcourses', views.allcourses, name='allcourses'),
    path('single', views.single, name='single'),
    path('editcourse', views.editcourse, name='editcourse'),
    path('deletecourse', views.deletecourse, name='deletecourse'),

]