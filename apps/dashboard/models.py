from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses')
    description = models.TextField(max_length=500)
    price = models.IntegerField()

