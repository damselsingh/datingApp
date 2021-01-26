from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    Bio = models.CharField(max_length=200)
    profileimage = models.ImageField(upload_to='images', blank=True, null=True)
    age = models.IntegerField()
    Hobbies = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)





