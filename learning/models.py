from django.db import models

# Create your models here.
class Milk(models.Model):
    milk_date = models.DateField(auto_now=True)
    milk_taken = models.BooleanField()
    milk_time = models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.milk_date)

class Setting(models.Model):
    price = models.IntegerField(default=40)

    def __str__(self):
        return "MRP"