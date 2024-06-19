from django.db import models
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=10)
    no_of_guests = models.IntegerField(default=0)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   inventory = models.IntegerField(default=0) 

   def __str__(self):
      return self.name