# 내부 뷰에 연결된 url 제어 
from django.urls import path 
from . import views # 동일한 폴더 views 연결 

urlpatterns = [
    path('', views.simple_view), # domain.com/first_app

]