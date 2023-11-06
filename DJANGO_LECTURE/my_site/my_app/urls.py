from django.urls import path 
from . import views 

urlpatterns = [
    # path 연결 /my_apps ---> PROJECT urls.py : 함수연결 방식
    path('', views.index, name='index')  
]