from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def success_stories(request):
    return render(request, 'success_stories.html')

def contact(request):
    return render(request, 'contact.html')