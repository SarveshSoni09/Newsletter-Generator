from django.shortcuts import render
from faculty_panel.models import *
from django.contrib import messages

# Create your views here.
def faculty_page(request):
    return render(request, 'faculty-panel.html')

def submit_data(request):
    if request.method == "POST":
        num = request.POST['array']
        num = num.split(',')
        faculty_highlights(request, num)
        remarkable_milestones(request, num)
        activities_conducted(request, num)
        placement_stats(request, num)
        student_achievements(request, num)
        events_faculties(request, num)
        project_companies(request, num)
        phd_faculties(request, num)
        messages.info(request, 'Data submitted succesfully')
        return render(request, 'faculty-panel.html')

def faculty_highlights(request, num):
    for x in range(int(num[0])+1):
        faculty_name = request.POST['faculty_name'+str(x)]
        achievement = request.POST['achievements'+str(x)]
        image = request.POST['high-img'+str(x)]
        if faculty_name != '' or achievement != '' or image != '':
            faculty_highlights = Highlights(faculty_name = faculty_name, achievement = achievement, image=image)
            faculty_highlights.save()

def remarkable_milestones(request, num):
    for x in range (int(num[1])+1):
        description = request.POST['milestones-desc'+str(x)]
        image = request.POST['milestones-img'+str(x)]
        if description != '' or image != '':
            remarkable_milestones = Milestones(description=description, image=image)
            remarkable_milestones.save()

def activities_conducted(request, num):
    for x in range (int(num[2])+1):
        description = request.POST['activitiess-desc'+str(x)]
        image = request.POST['activities-img'+str(x)]
        caption = request.POST['activities-cap'+str(x)]
        if description != '' or image != '' or caption != '':
            activities_conducted = Activities(description=description, image=image, caption=caption)
            activities_conducted.save()

def placement_stats(request, num):
    for x in range(int(num[3])+1):
        company = request.POST['placements-comp'+str(x)]
        number = request.POST['placements-num'+str(x)]
        if company != '' or number != '':
            placement_stats = Placements(company=company, number=number)
            placement_stats.save()

def student_achievements(request, num):
    for x in range (int(num[4])+1):
        description = request.POST['students-desc'+str(x)]
        image = request.POST['students-img'+str(x)]
        if description != '' or image != '':
            student_achievements = Students(description=description, image=image)
            student_achievements.save()

def events_faculties(request, num):
    for x in range (int(num[5])+1):
        description = request.POST['events-desc'+str(x)]
        image = request.POST['events-img'+str(x)]
        if description != '' or image != '':
            events_faculties = Events(description=description, image=image)
            events_faculties.save()

def project_companies(request, num):
    for x in range (int(num[6])+1):
        description = request.POST['projects-desc'+str(x)]
        if description != '':
            project_companies = Projects(description=description)
            project_companies.save()

def phd_faculties(request, num):
    for x in range (int(num[7])+1):
        description = request.POST['phd-desc'+str(x)]
        if description != '':
            phd_faculties = Phd(description=description)
            phd_faculties.save()



