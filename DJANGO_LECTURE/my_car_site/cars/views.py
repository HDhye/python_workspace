from django.shortcuts import render, redirect
from .models import Car 
from django.urls import reverse # 리다이렉트시 역주소 찾기 
from django.contrib import messages # 메세지 전달 

# Create your views here.
def list(request):
    
    all_cars = Car.objects.all() 
    
    
    return render(request, 'cars/list.html', context={'all_cars': all_cars})

def add(request):
    print(request.POST)
    if request.POST : 
       brand = request.POST['brand']
       year = request.POST['year']  
       Car.objects.create(brand=brand, year=year)
       
       # 새로운 차를 등록하면 리스트로 리다이렉트 
       return redirect(reverse('cars:list'))
    
    else: return render(request, 'cars/add.html')
    

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            Car.objects.get(pk=pk).delete()
            messages.success(request, '삭제 성공')
            
            return redirect(reverse('cars:list'))
        except Exception as e:
            messages.error(request, f'삭제 실패 : {str(e)}')  
            return render(request, 'cars/delete.html')
                      
    else : return render(request, 'cars/delete.html')


    
