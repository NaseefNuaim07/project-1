from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class trainer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class userr(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class place(models.Model):
    name = models.CharField(max_length=100)

class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class dive(models.Model):
    date = models.DateField(auto_now_add=True,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

