from django.shortcuts import render
from faculty_panel.models import Highlights
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
            if image in request.FILES: print("image there")
            faculty_highlights = Highlights(faculty_name = faculty_name, achievement = achievement, image=image)
            faculty_highlights.save()

def remarkable_milestones(request, num):
    pass

def activities_conducted(request, num):
    pass

def placement_stats(request, num):
    pass

def student_achievements(request, num):
    pass

def events_faculties(request, num):
    pass

def project_companies(request, num):
    pass

def phd_faculties(request, num):
    pass



