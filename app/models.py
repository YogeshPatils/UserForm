from django.db import models

# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=200,unique=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.IntegerField(unique=True)
    gender=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    re_password=models.CharField(max_length=100)
