from django.shortcuts import render, redirect
from django.http import HttpResponse
from project.forms import CustomUserCreationForm
from project.forms import CustomAuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  
    else:
            form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})  

def login(request):
    return render(request, 'login.html')