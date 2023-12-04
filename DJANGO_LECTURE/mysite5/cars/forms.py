from django import forms 
from .models import Review 
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First_name', max_length=100)   # input 라벨명, 사이즈 설정 -> 위젯 연결 - text input 
#     last_name = forms.CharField(label='Last_name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='리뷰를 입력해주세요.',
#                             widget=forms.Textarea(attrs={'class':'myform'
#                                                             , 'rows':'2', 'cols':'2'}))  # 태그속성 설정 

class ReviewForm(ModelForm):
    class Meta:
        model = Review # 모델이 있으니 그대로 폼을 만들라는 명령 
        # fields = ['first_name', 'last_name', 'stars']
        
        fields = "__all__" # 모든 필드 불러오기 
        
        # 오버라이딩 
        labels = {
            'first_name': '이름',
            'last_name': '성',
            'stars':'별점'
        }
        
        # 필드별 에러메세지 커스텀 
        error_messages = {
            'stars':{
                'min_value':"1 이상 이어야 합니다.",
                'max_value':"5 이하"
            }
        }