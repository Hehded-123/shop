from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="photos/%Y%m%d")
    created_at = models.DateTimeField(auto_now_add=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    message = models.TextField()