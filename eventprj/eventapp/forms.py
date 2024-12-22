from . models import Booking
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput()
        }

        labels = {'name':'Your Name',
                  'phone':'Phone/Mobile',
                  'event': 'Event',
                  'booking_date': 'Date of Event',
                  }