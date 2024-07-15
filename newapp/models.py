from django.db import models
from django.contrib.auth.models import User
import os

class Profile(models.Model):
    USER_TYPES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.user.username