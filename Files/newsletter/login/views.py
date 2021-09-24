from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth 
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=email, password=pwd)
        if user is not None:
            if request.user.is_superuser:
                auth.login(request, user)
                return redirect('admin-panel')
            else:
                auth.login(request, user)
                return redirect('faculty-panel')
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('/')
    else:
        return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def logout(request):
    auth.logout(request)
    return redirect('/')