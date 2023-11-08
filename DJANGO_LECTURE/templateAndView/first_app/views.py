from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# view template 연결 

articles = { 
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def simple_view(request):
    return render(request, 'first_app/example.html') # .html 