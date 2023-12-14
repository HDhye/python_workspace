from django.urls import path
# from .views import home_view 
from .views import (HomeView, ThankYouView, 
                    ContractFromView, TeacherCreateView,
                    TeacherListView, TeacherDetailView,
                    TeacherUpdateView, TeacherDeleteView)

app_name = 'classroom'

urlpatterns = [
    # path('',home_view, name='home') # 함수 기반 뷰를 기대한다.
    path('',HomeView.as_view(), name='home') # 클래스를 가지고 경로에 대한 함수를 반환한다.
    , path('thank_you/', ThankYouView.as_view(), name='thank_you')
    , path('contact/', ContractFromView.as_view(), name='contact')
    , path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher')
    , path('list_teacher/', TeacherListView.as_view(), name='list_teacher')
    , path('detail_teacher/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher')
    , path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher')
    , path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher')
]