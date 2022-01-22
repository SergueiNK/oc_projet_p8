from django.shortcuts import render, redirect
from .forms import CreateUserForm
from product.models import Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def user(request):
    """Display the page of user"""
    return render(request, 'user/user.html')


def registerPage(request):
    """Register user page"""
    form = CreateUserForm()
    # Take the input data from user register
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # Show the sucess message after user creating in login page
            messages.success(request, 'Le compte a été crée pour' + user)
            # Redirect to user login page
            return redirect('users:login')
        else:
            # User message
            messages.info(request, 'Merci de vous connecter')
    context = {'form': form}
    return render(request, 'user/register.html', context)


def loginPage(request):
    """Login user page"""
    if request.method == 'POST':
        # Take user input during login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            # If user exist connection is available
            login(request, user)
            return render(request, 'home/home.html')
        else:
            # Show message in case of error during login
            messages.info(
                request,
                'Le nom d\'utilisateur OU \
                 le mot de passe sont incorrectes')
    context = {}
    return render(request, 'user/login.html', context)


def logoutUser(request):
    """Logout user function"""
    logout(request)
    return redirect('users:login')


@login_required
def getUser(request):
    """Access user page"""
    return render(request, 'user/user.html')

@login_required
def getFavorite(request):
    """Acces substitute Favorite page"""
    # Take the user current id
    user = request.user.id
    # Take the objects in Favorite model relative the user current id
    favorite_id = Favorite.objects.filter(user_fk=user)
    # Append all products in user list
    product_favorite = []
    for product in favorite_id:
        product_favorite.append(product.product_fk)
    return render(
        request,
        'user/favorite_product.html',
        {"product_favorite": product_favorite})
