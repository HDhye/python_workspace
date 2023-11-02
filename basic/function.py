# 함수

# def 함수이름(파라미터): 
def name_of_function(parameter):
    # 구현내용
    print(f"function의 파라미터는 {parameter}")
    # 반환값 
    return parameter
# 들여쓰기 주의 
returning = name_of_function(2)
print(returning)

def say_hello():
    print("Hello")
    print("another Hello~!")

myvar = say_hello()
print(myvar) # None 리턴없음 

def say_hello2(name, age):
    return f"내 이름은 {name}이고, 나이는 {age}세입니다"

myvar2 = say_hello2('dahye',10)
print(myvar2)
# 순서상관없이 명시적으로 가능 
myvar3 = say_hello2(age=20, name='john')
print(myvar3) # 내 이름은 john이고, 나이는 20세입니다. 

mylist1 = [1,24,3,1,6,7,2,9,10,2]
mylist2 = [1,24,3,1,6,7,2,9,2]

def checker(list_to_check):
    for num in list_to_check:
        if num == 10:
            return True
    return False

print(checker(mylist1)) # True
print(checker(mylist2)) # False

# 두 값, a와 b를 "+" 또는 "-" 문자열 연산자를 허용하는 calculator라는 함수를 구현하세요. 함수는 'a 연산자 b'를 결과로 반환해야 합니다. (즉, a+b 또는 a-b)
def calculator(a, b, operation):
    if operation == '+' :
        return a + b 
    elif operation == '-':
        return a - b 
    
print(calculator(2, 3, "+")) # 5 
print(calculator(2, 3, '-')) # -1 