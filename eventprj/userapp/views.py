from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username already exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email already exists!")
                return redirect('register')
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password) 
                user_reg.save()   
                messages.info(request,"Registered Successfully!")            
                return redirect('/')
        else:
            messages.info(request,"Password doesn't match!")
            return redirect('register')    
    return render(request,'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password!") 
            return redirect('register')
    return render(request,'login.html') 

def logout(request):
    auth.logout(request)
    return redirect('/')