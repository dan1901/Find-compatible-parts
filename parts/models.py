from django.db import models

# Create your models here.
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"

class PartCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Part(models.Model):
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    original_part_name = models.CharField(max_length=100)
    original_part_number = models.CharField(max_length=100)
    compatible_part_name = models.CharField(max_length=100)
    compatible_part_number = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.original_part_name} - {self.car_model.name}"