from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def simple_view(request):
    return HttpResponse("simple view page")


def home_view(request):
    return HttpResponse("HOME VIEW~")