from django.db import models

# Create your models here.
class ProductModel(models.Model):
    prodname=models.CharField(max_length=255)
    quantity=models.IntegerField()
    description=models.CharField(max_length=255)
    price=models.IntegerField()