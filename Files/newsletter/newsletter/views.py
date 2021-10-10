from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth 
from admin_panel import views 
from admin_panel.models import *
from faculty_panel.models import *

def download_doc(request):
    if request.method=='GET':
        all_data = views.get_data()
        get_highlights(request, Highlights.objects.values())
        milestones = Milestones.objects.values()
        activities = Activities.objects.values()
        placements = Placements.objects.values()
        students = Students.objects.values()
        events = Events.objects.values()
        projects = Projects.objects.values()
        phds = Phd.objects.values()
        
           
    
    return render(request, 'admin-panel.html', {'all_data' : all_data})


def get_highlights(request, highlights):
    faculty_name = []
    achievement = []
    images = []
    ids_raw = highlights.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'highlights'+str(i)+'-check' in request.GET:
            faculty_name.append(Highlights.objects.get(pk=i).faculty_name)
            achievement.append(Highlights.objects.get(pk=i).achievement)
            images.append(Highlights.objects.get(pk=i).image)
    print(faculty_name, achievement, images)