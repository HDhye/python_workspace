from django.urls import path
# from .views import home_view 
from .views import HomeView, ThankYouView, ContractFromView

app_name = 'classroom'

urlpatterns = [
    # path('',home_view, name='home') # 함수 기반 뷰를 기대한다.
    path('',HomeView.as_view(), name='home') # 클래스를 가지고 경로에 대한 함수를 반환한다.
    , path('thank_you/', ThankYouView.as_view(), name='thank_you')
    , path('contact/', ContractFromView.as_view(), name='contact')
]