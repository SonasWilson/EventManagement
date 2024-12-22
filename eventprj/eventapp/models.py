from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='events')

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    booked_on = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name
    
