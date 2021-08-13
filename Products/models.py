from django.db import models
import datetime
# Create your models here.


class Product(models.Model):
    name        =  models.CharField( max_length=100)
    weight      =   models.FloatField()
    price       =   models.FloatField()
    created_date    =   models.DateField(verbose_name='created_date', auto_now_add=True)
    updated_date    =models.DateField(verbose_name='updated_date', auto_now=True)
    def __str__(self):
        return self.name
    