from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.
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
    
class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    prodcut_rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(max_length=100)
    date_reviewed = models.DateTimeField(default=timezone.now)