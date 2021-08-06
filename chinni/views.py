from django.shortcuts import render 
from django.http import HttpResponse 

def home(request):
    return HttpResponse("This is my first project on Django(simple project),later on i will learn all the concepts.@Seshu Nersu")

def second(request):
    return HttpResponse("Django is a web-development framework ,which uses python code internally and it works on MVT(Model,View,Template)Architecture")