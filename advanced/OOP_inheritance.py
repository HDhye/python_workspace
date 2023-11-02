# 상속 

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print('hello')

    def report(self):
        print(f"i am {self.first_name} {self.last_name}")

# 상속 클래스 
class Agent(Person):

    # 생략하면 부모 초기화 자동상속하여 지정된 파라미터만 사용함 
    def __init__(self, first_name, last_name, code_name):
        # 부모클래스의 초기화 상속 
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name 

    # override
    def report(self):
        print("overriding - i am here")

    def reveal(self, passcode):
        if passcode == 123:
            print('I am a secret agent!')
        else:
            self.report()  
    

# x = Person("Hwang", "Dahye")
# x.report() # i am Hwang Dahye
# x.reveal() # error - AttributeError: 'Person' object has no attribute 'reveal'  자식클래스 메소드임 

x = Agent("John", "Smith", "code.X")
x.reveal(123)
x.report() # 부모클래스 메소드 사용 가능 & 오버라이딩 
print(x.first_name)
print(x.code_name)

# 이름(name)과 종족(species)을 가진 Animal 클래스를 만드세요.
# 그 클래스에 greet()라는 함수를 만들어
# "Hi! My name is {name} and I am a {species}"라는 구문을 출력하세요.
# 그런 다음, 이 클래스를 사용하여 Cat과 Dog 클래스를 만드세요. 
# 각 클래스는 이름(name)을 인자로 받으며,
# 이 동물이 일반적으로 내는 소리를 출력하는 sound()라는 메서드를 구현하세요.("ruff"와 같은 문자열로).

class Animal():

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

class Cat(Animal):
    
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")

    def sound(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
        
    def sound(self):
        print("Wuff")

cat = Cat("냐옹이")
cat.sound()
dog = Dog("뭉뭉이")
dog.sound()