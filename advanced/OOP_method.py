# 메소드 

class Circle():
    
    pi = 3.14 

    def __init__(self, radius=1): # default가 1 
        self.radius = radius

    # 원 넓이 
    def area(self):
        result = pow(self.radius, 2) * self.pi
        return result
    
    # 원 둘레 
    def perimeter(self):
        return self.radius * 2 * self.pi

mycircle = Circle(radius=4)
print(mycircle.radius) # 4
print(mycircle.area()) # 50.24
print(mycircle.perimeter()) # 25.12

# 개의 이름, 품종 및 나이를 가진 Dog 클래스를 만드세요. 
# 개의 나이에 7을 곱하여 사람 나이로 계산한 나이를 구하여 결과로 반환하는 calculate_human_age라는 메서드를 정의하세요.
# calculate_human_age메서드는 self 이외의 인자를 받지 말아야 합니다.
# 이 클래스를 사용하여 "Hans"라는 7살 짜리 "저먼 셰퍼드"를 만들고, 그 개의 "인간 나이"를 알아보세요.
class Dog():

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed 
        self.age = age

    def calculate_human_age(self):

        return self.age * 7 

dog = Dog('Hans', '저먼 셰퍼드', 7)
print(dog.calculate_human_age())