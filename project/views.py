from django.shortcuts import render, redirect
from django.http import HttpResponse
from project.forms import CustomUserCreationForm
from project.forms import CustomAuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_failure
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'index.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  
    else:
            form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})  


@csrf_failure
def customer_csrf_failure_view(request, reason=""):

    return HttpResponseForbidden('CSRF verification failed. Please Try again.')


def login(request):
    return render(request, 'login.html')