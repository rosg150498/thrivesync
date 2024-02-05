from django.shortcuts import render, redirect
from django.http import HttpResponse
from project.forms import CustomUserCreationForm
from project.forms import CustomAuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')