from django.db import models

# Create your models here.
class Patient(models.Model):
    # 열(컬럼)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField() # 유효성 검사 설정 
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name} is {self.age} years old."
    
    