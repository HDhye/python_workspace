# 내부 뷰에 연결된 url 제어 
from django.urls import path 
from . import views # 동일한 폴더 views 연결 

urlpatterns = [
    # /first_app/ 비워두면 프로젝트 레벨에서 정의된 모든것에 추가됨 
    # path('', views.simple_view)
    path('simple_view', views.simple_view),
]