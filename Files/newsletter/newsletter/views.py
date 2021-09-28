from django.shortcuts import render


def submit_data(request):
    if request.method == "POST":
        print("Button working")
        return render(request, 'faculty-panel.html')

