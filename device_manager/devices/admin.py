from django.contrib import admin
from .models import Device, Service, Measurement

# Register your models here.
admin.site.register(Device)
admin.site.register(Service)
admin.site.register(Measurement)