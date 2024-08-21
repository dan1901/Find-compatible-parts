
# Register your models here.
from django.contrib import admin
from .models import Manufacturer, CarModel, PartCategory, Part

admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(PartCategory)
admin.site.register(Part)