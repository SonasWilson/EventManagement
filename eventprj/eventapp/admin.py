from django.contrib import admin
from .models import Event,Booking
# Register your models here.

admin.site.register(Event)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'event','booking_date', 'booked_on')
admin.site.register(Booking,BookingAdmin)