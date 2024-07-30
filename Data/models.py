from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=10,null=True)
    phone=models.PositiveIntegerField(null=True)
    address=models.CharField(max_length=100,default="NA")

# Create your models here.
