from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Userdetail(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fb_link = models.CharField(max_length=200, null=True)
    tw_link = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='dp', null=True)
    phone_number = models.CharField(max_length=12, null=True)
    specialize = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    about = models.TextField(max_length=1000, null=True)
    views = models.CharField(max_length=200, null=True)
    reviews = models.CharField(max_length=200, null=True)
    followers = models.CharField(max_length=200, null=True)
    following = models.CharField(max_length=200, null=True)
    students = models.CharField(max_length=200, null=True)


    def __str__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)



class Course(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses')
    description = models.TextField(max_length=500)
    price = models.IntegerField()

