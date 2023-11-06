from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


# def simple_view(request):
#     return HttpResponse("simple view page")

# 동적 뷰 url 설정 

articles = { 
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2 
    addrst = num1 + num2 
    result = f"{num1} + {num2} = {addrst}"
    return HttpResponse(str(result)) 
