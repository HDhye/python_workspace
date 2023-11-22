from django.db import models

# Create your models here.
class Car(models.Model):
    
    # pk 
    
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    
    def __str__(self):
        
        return f"브랜드명 : {self.brand}, 연도 : {self.year}"
