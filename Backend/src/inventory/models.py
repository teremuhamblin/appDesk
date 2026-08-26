from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
