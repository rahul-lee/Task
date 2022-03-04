from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    productname = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.productname

    