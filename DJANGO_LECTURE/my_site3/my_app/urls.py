from django.urls import path
from . import views

# 1. app 이름 등록 
# 2. URL Names 
#  
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
]