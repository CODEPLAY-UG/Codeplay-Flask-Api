from email import message
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model
from django.conf import settings
from django.dispatch import receiver
User = settings.AUTH_USER_MODEL
# Create your views here.
class User(AbstractUser):
    username = models.CharField(max_length=55, unique=True, null=True) 
    contact = models.CharField(max_length=14, null=True)  
    #ProfilePic = CloudinaryField('image')
    first_name = models.CharField(max_length=55,null=True)
    last_name = models.CharField(max_length=55,null=True)
    gender = models.CharField(max_length=55, null=True)
    email = models.EmailField(default=True)
    Date = models.DateField(auto_now=True)
    is_codeplay_admin = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Messages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)