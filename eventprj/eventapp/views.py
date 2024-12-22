from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def events(request):
    event = {
        'event':Event.objects.all()
    }
    return render(request,'events.html',event)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()    
    return render(request,'booking.html',{'form':form})


def contact(request):
    return render(request,'contact.html')