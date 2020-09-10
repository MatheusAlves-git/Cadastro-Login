from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User, UserManager
#from django.views import generic
#from django.views.generic.edit import CreateView
#from django.urls import reverse_lazy
#from django.contrib.auth import authenticate, login

# Create your views here.


def loginPage(request):
    return redirect('http://127.0.0.1:8000/accounts/login/')


def registerPage(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})


@login_required()
def dashboardPage(request):
    return render(request, 'dashboard.html')