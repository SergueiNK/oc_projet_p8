from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'user/user.html')

def create(request):
    return render(request, 'user/create.html')

def login(request):
    return render(request, 'user/login.html')