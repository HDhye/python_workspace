# 내장함수 

# len() 길이 
mylist = [1,2,3]
print(len(mylist)) # 3

# __str__(), __len__() 객체 자체적인 문자열과 길이를 지정한다.

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages 

    # toString overrride 한것과 비슷함 
    def __str__(self):      
    # 문자열 return 필수 
        return f"{self.title} written by {self.author}"

    # __len__() : int 리턴 
    def __len__(self):
        return self.pages

mybook = Book('python', 'hdh', 120)
# print(len(mybook)) # TypeError: object of type 'Book' has no len()
print(mybook) # python written by hdh --> 자바에서 toString overrride 한것과 비슷함 
print(len(mybook)) # 120 

# names라는 이름 리스트를 인자로 받는 Students 클래스를 만듭니다.
# 클래스 객체가 보유하고 있는 학생 수를 반환하는 함수와 인스턴스를 출력하려는 경우 발생하는 것을 정의하는 또다른 함수를 구현하세요. 
# 출력할 때 모든 학생의 이름이 표시되어야 합니다.

class Students():

    def __init__(self, names):
        self.names = names 

    def __str__(self):
        return f"{self.names}"
    
    def __len__(self):
        return len(self.names)

names = ['john', 'andy', 'kim', 'park']
x = Students(names)
print(x)
print(len(x))