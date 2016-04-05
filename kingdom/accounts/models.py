from django.db import models

# Create your models here.

class customer(models.Model):
    username = models.CharField(max_length=30)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    iconurl = models.CharField(max_length=255)

