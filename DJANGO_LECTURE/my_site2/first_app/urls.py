# 내부 뷰에 연결된 url 제어 
from django.urls import path 
from . import views # 동일한 폴더 views 연결 

urlpatterns = [
    # /first_app/ 비워두면 프로젝트 레벨에서 정의된 모든것에 추가됨 
    # path('', views.simple_view)
    # path('simple_view', views.simple_view),
    # path('sports/', views.sports_view), #http://127.0.0.1:8000/first_app/sports/
    # path('finance/', views.finance_view) #http://127.0.0.1:8000/first_app/finance/
    
    # 동적 url 라우팅 설정 
    path('<str:topic>/', views.news_view) # string 타입 설정, 비워두면 모든타입 
    , 
    path('<int:num1>/<int:num2>', views.add_view)
]