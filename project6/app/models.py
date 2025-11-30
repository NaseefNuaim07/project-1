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
    places = models.ForeignKey(place,on_delete=models.CASCADE,null=True)
    categorys = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    status=models.CharField(default='pending')
    trainer_id= models.ForeignKey(trainer,on_delete=models.CASCADE,null=True)
    count=models.IntegerField(default=1)


class DiveMedical(models.Model):
    booking = models.ForeignKey(dive, on_delete=models.CASCADE, related_name="medical_forms")

    full_name = models.CharField(max_length=150)
    dob = models.DateField()
    experience_level = models.CharField(max_length=50)

    emergency_name = models.CharField(max_length=150)
    emergency_phone = models.CharField(max_length=20)

    # saving multiple conditions as CSV (from checkbox list)
    conditions = models.TextField(blank=True)

    medical_details = models.TextField(blank=True)

    physician = models.CharField(max_length=150, blank=True)
    recent_dive = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)


    # Helper function to convert CSV → list
    def conditions_list(self):
        if self.conditions:
            return self.conditions.split(",")
        return []

    def __str__(self):
        return f"Medical Form for {self.full_name} (Booking {self.booking.pk})"
