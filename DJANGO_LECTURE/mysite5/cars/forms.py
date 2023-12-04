from django import forms 

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First_name', max_length=100)   # input 라벨명, 사이즈 설정 -> 위젯 연결 - text input 
    last_name = forms.CharField(label='Last_name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='리뷰를 입력해주세요.',
                            widget=forms.Textarea(attrs={'class':'myform'
                                                            , 'rows':'2', 'cols':'2'}))  # 태그속성 설정 
    