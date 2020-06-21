from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
         return self.name
class Employee(models.Model):
    name=models.CharField(max_length=50) 
    email=models.EmailField(default='')
    img=models.FileField(upload_to='pic/',default=None)
    def __str__(self):
        return self.name    
class Users(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
         return self.name        