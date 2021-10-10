from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth

from admin_panel.views import get_data 
# Create your views here.


def login(request):
    all_data = get_data()
    return render(request, 'admin-panel.html', {'all_data' : all_data})

    # if request.method == 'POST':
    #     email = request.POST['email']
    #     pwd = request.POST['pwd']
    #     user = auth.authenticate(username=email, password=pwd)
    #     if user is not None:
    #         if user.is_superuser:
    #             auth.login(request, user)
    #             # return redirect('admin-panel')
    #             return render(request, 'admin-panel.html', {'all_data' : all_data})
    #         else:
    #             auth.login(request, user)
    #             # return redirect('faculty-panel')
    #             return render(request, 'faculty-panel.html')
                
    #     else:
    #         messages.info(request, 'Invalid email or password')
    #         return redirect('/')
    # else:
    #     return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def logout(request):
    auth.logout(request)
    return redirect('/')