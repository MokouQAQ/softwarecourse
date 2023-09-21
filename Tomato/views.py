from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def show_home(request):
    return render(request, 'home.html', )