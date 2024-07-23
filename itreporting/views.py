from django.shortcuts import render
from .models import Request

# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})

def requests(request):
    daily_report = {'requests': Request.objects.all(), 'title': 'Requests Made'}
    return render(request, 'itreporting/requests.html', daily_report)