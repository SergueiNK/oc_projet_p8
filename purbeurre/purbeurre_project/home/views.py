from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def legal_notice(request):
    return render(request, 'home/legal.html')