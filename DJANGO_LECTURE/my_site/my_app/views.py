from django.shortcuts import render
#http 응답 
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("my_app 뷰화면")