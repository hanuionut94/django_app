from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_users(request):
    return render(request, 'authenticate/login.html', {})