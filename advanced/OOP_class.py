# 클래스와 속성

# num = 10
# var = '10'
# print(type(num)) # class 'int'
# print(type(var)) # class 'str'

class Sample(): # () 안해도 된다 
    pass # 정의 외에는 아무것도 하지 말라는 키워드 (초기화 등 안함) 

num = Sample()
print(type(num)) # <class '__main__.Sample'


class Sample2():
    # 초기화 매서드(생성자) 
    def __init__(self, name): # 언더바는 2개씩 
        self.name = name # this == self 


x = Sample2('john') # 주어진 파라미터에 맞게 초기화해야함
print(type(x)) # <class '__main__.Sample2'>
print(x.name) # john - 초기화 된 결과 

class Student():

    # 모든 인스턴스에 대해 동일한 값 = 클래스 객체 속성 (클래스 정적 변수)  
    planet = 'Earth'

    def __init__(self, name, gpa):
        # 모든 인스턴스가 다 다른 값 (self 속성 할당) 동적 변수 
        self.name = name
        self.gpa = gpa

stu1 = Student('Jose', 4.0)
stu2 = Student(name="Mina", gpa=3.8)
print(stu1) # <__main__.Student object at 0x104ef1a90>
print(stu1.gpa) # 4.0
print(stu1.planet) # Earth 

class Agent:

    origin = 'KOREA'

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
x = Agent('Kim', 6, 160)
print(x.weight)
x.weight = 180 # 인스턴스 메서드 속성 변경 
print(x.weight)
x.origin = 'USA'
print(x.origin) # USA 
x2 = Agent('Lee', 10, 190)
print(x2.origin) # KOREA

# 개의 이름과 품종을 갖는 Dog 클래스를 만드세요.
#  이 클래스를 사용하여 "Hans"라는 "저먼 셰퍼드"종과 "Lou"라는 "레브라도"종의 두 마리의 Dog 객체를 만드세요. 
# 마지막으로 f-string을 사용하여 "Hans and Lou are friends”라는 문구 내에 두 마리 개의 이름을 출력하세요. 
# (var.name과 같이 속성 호출을 사용)

class Dog():

    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed

dog1 = Dog("Hans", "저먼 셰퍼드")
dog2 = Dog("Lou", "레브라도")
print(f"{dog1.name} and {dog2.name} are friends") 
