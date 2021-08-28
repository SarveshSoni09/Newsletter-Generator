from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth 

# Create your views here.
def registration(request):
    if request.method == "POST":    
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        conpwd = request.POST['conpwd']
        dept = request.POST['dept']
        if User.objects.filter(username=email).exists():
            messages.info(request, 'Email already registered')
            return redirect('registration')
        else:
            user = User.objects.create_user(username=email, password=pwd, email=email, first_name=fname, last_name=lname)
            user.save()
            print('THIS SHIT IS WORKING !!!')
            return redirect('/')
            
    else:
        return render(request, 'signUp.html')