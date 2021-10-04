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
        for x in range(int(num[0])):
            faculty_name = request.POST['faculty_name'+str(x)]
            achievement = request.POST['achievements'+str(x)]
            image = request.POST['high-img'+str(x)]
            faculty_highlights = Highlights(faculty_name = faculty_name, achievement = achievement, image=image)
            faculty_highlights.save()
        messages.info(request, 'Data submitted succesfully')
        return render(request, 'faculty-panel.html')