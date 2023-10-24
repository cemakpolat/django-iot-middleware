from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Device(BaseModel):
    device_id = models.CharField(max_length=100, unique=True)
    # Add other device properties
    services = models.ManyToManyField('Service', related_name='devices')
    def __str__(self):
        return self.device_id


class Measurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.FloatField()
    # Add other measurement properties

class Service(models.Model):
    name = models.CharField(max_length=100)
    # Add other service properties

# class Smartspace(models.Model):
#     name = models.CharField(max_length=100)
#     # Add other fields specific to Smartspace

#     def __str__(self):
#         return self.name


# class Device(BaseModel):
#     device_id = models.CharField(max_length=50, unique=True)
#     name = models.CharField(max_length=100)
#     # Add other fields specific to Device

#     smartspace = models.ForeignKey(Smartspace, on_delete=models.CASCADE)
#     # Add other fields and methods as needed

#     def __str__(self):
#         return self.name



# class DeviceService(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     devices = models.ManyToManyField(Device)
#     # Add other fields and methods as needed

#     def __str__(self):
#         return self.name

# class SpaceService(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     spaces = models.ManyToManyField(Smartspace)
#     # Add other fields and methods as needed

#     def __str__(self):
#         return self.name