from django.db import models

# Create your models here.
class Pool(models.Model):
    providers = models.ManyToManyField(Providers)
    product = models.ForeignKey(Products)
    suppliers = models.ManyToManyField(Suppliers)

    def __str__(self):
        return self.product.title
