from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=50, null=True)
    release_of_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f' The Product is a {self.name} '

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f' Profile for {self.user.username} '


# Create your models here.
