from django.db import models

# Create your models here.


class NotBaseModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    name2 = ["Adrian"]