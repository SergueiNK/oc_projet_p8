from django.shortcuts import render


def home (request):
    """test the home page"""
    return render(request, 'home/home.html')

def legal_notice(request):
    """test the leagal notice page"""
    return render(request, 'home/legal.html')