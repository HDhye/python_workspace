from django.shortcuts import render
from django.urls import reverse_lazy  

# 폼뷰를 일반뷰(generic view)로 임포트 
from django.views.generic import TemplateView, FormView

# 폼을 뷰에 임포트 
from classroom.forms import ContactForm


# Create your views here.

# 함수 기반 뷰 
def home_view(request):
    return render(request, 'classroom/home.html')


# 클래스 기반 뷰 
class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'
    
class ContractFromView(FormView):
    # 속성 
    form_class = ContactForm # 연결한 폼 클래스
    template_name = 'classroom/contact.html' # 폼을 보내는 템플릿 네임
    
    # success URL(이동하려는 주소 - 템플릿 아님)
    success_url = reverse_lazy('classroom:thank_you') #thankyou.html
    
    # what to do with Form
    def form_valid(self, form):
        print(form.cleaned_data)
        
        # ContactForm(request.POST)
        return super().form_valid(form)    
    
    
    