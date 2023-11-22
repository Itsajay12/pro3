from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisterUser(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # fname=models.CharField( max_length=50)
    # lname=models.CharField( max_length=50)
    # uname=models.CharField( max_length=50)
    # email=models.EmailField( max_length=154)
    # password=models.CharField(max_length=50)
  