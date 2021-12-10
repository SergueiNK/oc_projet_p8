from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
#from .models import AuthUser
from django.contrib.auth.models import User
from product.models import Favorite
from django.contrib.auth.decorators import login_required
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
            #return redirect('users:user')
            return render(request, 'home/home.html')
        else:
            messages.info(request, 'Le nom d\'utilisateur OU le mot de passe sont incorrectes')

    context = {}
    return render(request, 'user/login.html', context)

# Need to finalise the navbar
def logoutUser(request):
    logout(request)
    return redirect('users:login')

# Pas besoin revoir method Django request.user model gestion utilisateur Django
@login_required
def getUser(request):
 
    return render(request, 'user/user.html')

def getFavorite (request):

    # Besoin de voir pourquoi un seul objet s'affiche et non les trois
    user = request.user.id
    favorite_id = Favorite.objects.filter (user_fk = user)
    #print(favorite_id)
    product_favorite= [] 
    for product in favorite_id:
        product_favorite.append(product.product_fk)
        #print(product_favorite)
        
    return render (request, 'user/favorite_product.html', {"product_favorite": product_favorite})