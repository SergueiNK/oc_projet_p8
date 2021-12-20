from django.shortcuts import render, redirect
from .forms import CreateUserForm
from product.models import Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
def user(request):
    return render(request, 'user/user.html')

def registerPage(request):
    form = CreateUserForm()
    # On récoit les données de navigateur pour la création de compte
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte a été crée pour' + user)
            return redirect('users:user')
        else:
            messages.info(request, 'Merci de vous connecter')    
    context = {'form':form}
    return render(request, 'user/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/home.html')
        else:
            messages.info(request, 'Le nom d\'utilisateur OU le mot de passe sont incorrectes')
    context = {}
    return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('users:login')

@login_required
def getUser(request):
    return render(request, 'user/user.html')

def getFavorite(request):

    user = request.user.id
    favorite_id = Favorite.objects.filter (user_fk = user)
    product_favorite= [] 
    for product in favorite_id:
        product_favorite.append(product.product_fk)    
    return render (request, 'user/favorite_product.html', {"product_favorite": product_favorite})