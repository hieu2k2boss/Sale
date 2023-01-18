from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default="",max_length=100)
    slug = models.CharField(default="100",max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    
class Product(models.Model):
    title = models.CharField(default="",max_length=200)
    description = models.TextField(default='')
    price = models.IntegerField(default=0) 
    active = models.BooleanField(default=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    
class Variation(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(default="",max_length=200)
    price = models.IntegerField(default=0) 
    price_sale = models.IntegerField(default=0) 
    active = models.BooleanField(default=True)