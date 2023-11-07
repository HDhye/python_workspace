from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
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
    try: 
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404") # 404.html 템플릿, 배포시 debug false설정하기  

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2 
    addrst = num1 + num2 
    result = f"{num1} + {num2} = {addrst}"
    return HttpResponse(str(result)) 

# 리다이렉트 
# domain.com/first_app/0 ---> domain.com/first_app/sports 
def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]
    print(f"======={topic}=======")
    #리다이렉트 
    # return HttpResponseRedirect(topic) # hard cording 

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))

