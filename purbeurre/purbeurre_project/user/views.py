from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def user(request):
    return render(request, 'user/user.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'user/register.html', context)

def login(request):
    context = {}
    return render(request, 'user/login.html', context)