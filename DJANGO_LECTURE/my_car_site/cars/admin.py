from django.contrib import admin
from cars.models import Car  # app - model 임포트 

# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):  # model Name + Admin 
    # 필드 순서 변경 
    fields  = ['year', 'brand']
    
    # 필드셋 - 세그먼트화 
    # fieldsets = [
    #     ('TIME INFORMATION', {'fields' : ['year']}),
    #     ('CAR INFORMATION', {'fields': ['brand']}) 
    # ]
admin.site.register(Car, CarAdmin)