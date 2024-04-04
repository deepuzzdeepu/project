from django.db import models

# Create your models here.


# models.py
from django.db import models

class SensorData(models.Model):
    sensor = models.CharField(max_length=255)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor}: {self.value}"
