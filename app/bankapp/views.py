from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home():
    return HttpRequest('<h2> home </h2>')
