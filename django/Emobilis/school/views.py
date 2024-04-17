from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('welcome to Emobilis'),

def about(request):
    return HttpResponse('this is about page')


# Create your views here.
