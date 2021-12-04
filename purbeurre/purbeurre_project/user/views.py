from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import AuthUser
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
def user(request):
    return render(request, 'user/user.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte a été crée pour' + user)
            return redirect('users:user')
        else:
            messages.info(request, 'le le le')    

    context = {'form':form}
    return render(request, 'user/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #return redirect('users:userDetails')
            return redirect('users:user')
        else:
            messages.info(request, 'Le nom d\'utilisateur OU le mot de passe sont incorrectes')

    context = {}
    return render(request, 'user/login.html', context)

# Need to finalise the navbar
def logoutUser(request):
    logout(request)
    return redirect('users:login')

def getUser(request, id):
    user_data={}

    if request.method == 'GET':
        user_data=AuthUser.objects.get(id=id)
        print(user)
        return render(request, 'user/user.html', {'user_data': user_data})
