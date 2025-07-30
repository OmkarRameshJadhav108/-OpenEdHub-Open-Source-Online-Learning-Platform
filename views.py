from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World!")



def home(request):
    return render(request, 'myapp/home.html')
from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.all()
    return render(request, 'myapp/home.html', {'courses': courses})

