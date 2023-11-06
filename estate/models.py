from django.db import models

class RealEstateProperty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    postcode = models.CharField(max_length=10)
    date_availability = models.DateField()
    expected_price = models.FloatField()
    selling_price = models.FloatField()
    bedrooms = models.IntegerField()
    living_area = models.IntegerField()
    facades = models.IntegerField()
    garage = models.BooleanField()
    garden = models.BooleanField()
    garden_area = models.IntegerField()
    garden_orientation = models.CharField(max_length=255)
    kitchen_type = models.CharField(max_length=255)
