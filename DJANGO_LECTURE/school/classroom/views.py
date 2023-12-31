from django.shortcuts import render
from django.urls import reverse_lazy  

# 폼뷰를 일반뷰(generic view)로 임포트 
from django.views.generic import (TemplateView, FormView, 
CreateView, ListView, DetailView, UpdateView, DeleteView)

# 폼을 뷰에 임포트 
from classroom.forms import ContactForm
from classroom.models import Teacher 
 
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
    # success_url = '/classroom/thank_you/' 
    success_url = reverse_lazy('classroom:thank_you') #thankyou.html
    
    # what to do with Form
    def form_valid(self, form):
        print(form.cleaned_data)
        
        # ContactForm(request.POST)
        return super().form_valid(form)    
    

# Create View 
class TeacherCreateView(CreateView):
    # model_form.html 연결 
    
    model = Teacher # 사용 모델  
    
    # 모델뷰에서는 submit 버튼을 누르면 save() 동작을 한다.
    fields = "__all__"
    
    # 성공시 반환 주소 
    success_url = reverse_lazy("classroom:thank_you")
    
# List View 
class TeacherListView(ListView):
    # model_list.html 연결 
    
    model = Teacher # 모델 인스턴스  
    
    # 쿼리속성 재정의(오버라이드)
    queryset = Teacher.objects.order_by('first_name') # 정렬 
    
    context_object_name = 'teacher_list' # 뷰에 전달될 컨텍스트 네이밍 
    

# Detail View 
class TeacherDetailView(DetailView):
    # model_detail.html
    
    model = Teacher 
    
    # 하나의 모델 아이템만 반환
    # pk --> {{ teacher }}
     
# Update View 
class TeacherUpdateView(UpdateView):
    # form -> 디테일뷰 기반 템플릿 자동 연결함 
    
    model = Teacher 
    # fields = "__all__" # 전체 가져오기 
    fields = ['last_name', 'subject'] # 이름과 과목만 수정 가능하게 폼 설정  
    
    success_url = reverse_lazy("classroom:list_teacher")
    
    
# Delete View
class TeacherDeleteView(DeleteView):
    # form --> 삭제확인 버튼 폼 = model_confirm_delete.html 자동연결
    model = Teacher 
    
    success_url = reverse_lazy("classroom:list_teacher")
    