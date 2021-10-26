from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from django.core.mail import send_mail

from login.views import login


# Create your views here.
global userid 
userid = ''
global password 
password = ''
randnum = random.randrange(999999)
def forgot_pass(request):
        check = send_otp(request)
        if check:
            return render(request, 'reset-password.html')
        else:
            return render(request, 'forgot-password.html')

def send_otp(request):
    message = ''
    if request.method == 'POST':
            email = request.POST['email']
            pwd = request.POST['pwd']
            con_pwd = request.POST['con_pwd']

            check1 = check2 = check3 = True
            if email == '' or pwd == '' or con_pwd == '':
                message = "Please fill all fields"
                check1 = False
            if not User.objects.filter(username=email).exists():
                message = "User does not exist"
                check2 = False
            if pwd != con_pwd:
                message = "Passwords do not match"
                check3 = False
            
            if check1 and check2 and check3:
                global userid
                userid = email
                global password
                password = pwd

                subject = 'Password Reset - Newsletter Generator'
                mail_message = 'The One Time Password for reseting you newsletter generator password is '+str(randnum)
                from_email = 'noreply.newsletter.somaiya@gmail.com'
                to_email = [email]
                send_mail(subject, mail_message, from_email, to_email, fail_silently = False)
                return True
    else:
        messages.info(request, message)
        return False

def reset_pass(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if int(otp) == randnum:
            user = User.objects.get(username=userid)
            user.set_password(password)
            user.save()
            message = "Password Reset Successful, please return to login"
        else: 
            message = "Invalid OTP"
            print(otp)
        messages.info(request, message)
        return render(request, 'reset-password.html')
    else:
        return render(request, 'index.html')
    
    

