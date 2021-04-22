from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="photos/%Y%m%d")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


