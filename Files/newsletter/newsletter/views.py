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
        get_milestones(request, Milestones.objects.values())
        get_activities(request, Activities.objects.values())
        get_placements(request, Placements.objects.values())
        get_students(request, Students.objects.values())
        get_events(request, Events.objects.values())
        get_projects(request, Projects.objects.values())
        get_phds(request, Phd.objects.values())
        
           
    
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

def get_milestones(request, milestones):
    milestone_desc = []
    images = []
    ids_raw = milestones.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'milestones'+str(i)+'-check' in request.GET:
            milestone_desc.append(Milestones.objects.get(pk=i).description)
            images.append(Milestones.objects.get(pk=i).image)
    print(milestone_desc, images)

def get_activities(request, activities):
    activity_desc = []
    images = []
    ids_raw = activities.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'activities'+str(i)+'-check' in request.GET:
            activity_desc.append(Activities.objects.get(pk=i).description)
            images.append(Activities.objects.get(pk=i).image)
    print(activity_desc, images)

def get_placements(request, placements):
    companies = []
    number = []
    ids_raw = placements.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'placements'+str(i)+'-check' in request.GET:
            companies.append(Placements.objects.get(pk=i).company)
            number.append(Placements.objects.get(pk=i).number)
    print(companies, number)

def get_students(request, students):
    student_desc = []
    images = []
    ids_raw = students.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'students'+str(i)+'-check' in request.GET:
            student_desc.append(Students.objects.get(pk=i).description)
            images.append(Students.objects.get(pk=i).image)
    print(student_desc, images)
    
def get_events(request, events):
    event_desc = []
    images = []
    ids_raw = events.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'events'+str(i)+'-check' in request.GET:
            event_desc.append(Events.objects.get(pk=i).description)
            images.append(Events.objects.get(pk=i).image)
    print(event_desc, images)

    
def get_projects(request, projects):
    project_desc = []
    ids_raw = projects.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'projects'+str(i)+'-check' in request.GET:
            project_desc.append(Projects.objects.get(pk=i).description)
    print(project_desc)

def get_phds(request, phds):
    phd_desc = []
    ids_raw = phds.values_list('id')
    ids = [j[0] for j in ids_raw]
    for i in ids:
        if 'phds'+str(i)+'-check' in request.GET:
            phd_desc.append(Phd.objects.get(pk=i).description)
    print(phd_desc)


