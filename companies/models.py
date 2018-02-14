from django.db import models

# Create your models here.


class PharmaceuticalCompanies(models.Model):
    name = models.CharField(blank=True, max_length=255)
    contact_person = models.CharField(blank=True, max_length=255)
    phone = models.PhoneNumberField(blank=True)
    email = models.EmailField()
    address = models.TextField(blank=True)
    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)
    zipcode = models.CharField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # products = models.ManyToManyField(Products)


    def __str__(self):
        return self.name
