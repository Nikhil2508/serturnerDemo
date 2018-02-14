from django.db import models

# Create your models here.
class Potentials(models.Model):
    products = models.ManyToManyField(products)
    company_name = models.CharField(blank=True, max_length=255)
    contact_person = models.CharField(blank=True, max_length=255)
    added = models.DateTimeField(auto_now_add=True)
    target_due_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.products.title
