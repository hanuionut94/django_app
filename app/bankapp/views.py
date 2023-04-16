from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html')

