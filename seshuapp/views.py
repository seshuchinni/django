from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homes(request):
    return HttpResponse("This is my firstapp")
