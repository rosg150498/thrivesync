from django.shortcuts import render, redirect
from django.http import HttpResponse
from project.forms import CustomUserCreationForm
from project.forms import CustomAuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  
    else:
            form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})  


def custom_csrf_failure_view(request, reason=""):

    return HttpResponseForbidden('CSRF verification failed. Please Try again.')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  

        form = CustomAuthenticationForm()
    
    return render(request, 'login.html',)