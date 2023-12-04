from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

def rental_review(request):
    
    # Post Request ----> Form Contents --> Thank_you 
    if request.method == 'POST':
        form = ReviewForm(request.POST)   # 포스트 요청이면 해당 폼데이터 전달 
        
        if form.is_valid():  # 유효한 폼인지 확인 
            #{'first_name:'Jose',}
            # print(form.cleaned_data)
            
            form.save()  # 모델 인스턴스로 전달된 폼 데이터 저장           
        
            # redirect
            return redirect(reverse('cars:thank_you'))    
    
    # render Form  
    else: 
        form = ReviewForm()   # 겟 요청이면 폼 페이지만 전달 

    return render(request, 'cars/rental_review.html', context={'form':form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')