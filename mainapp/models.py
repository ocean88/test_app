from django.db import models

# Create your models here.
from django.db import models
from django_countries.fields import CountryField


class Factory(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class RetailNetwork(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='retail_networks')
    debt_to_factory = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Entrepreneur(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    retail_network = models.ForeignKey(RetailNetwork, null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='entrepreneurs')
    factory = models.ForeignKey(Factory, null=True, blank=True, on_delete=models.CASCADE, related_name='entrepreneurs')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    factory = models.OneToOneField(Factory, null=True, blank=True, on_delete=models.CASCADE, related_name='product')
    retail_network = models.OneToOneField(RetailNetwork, null=True, blank=True, on_delete=models.CASCADE,
                                          related_name='product')
    entrepreneur = models.OneToOneField(Entrepreneur, null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='product')

    def __str__(self):
        return f"{self.name} - {self.model}"
