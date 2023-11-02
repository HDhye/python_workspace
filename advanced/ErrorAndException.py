# 오류 및 예외처리

# try, except, finally 

# SyntaxError 
# print("hello) 

#TypeError
# print("10" + 10)

try: 
    print("firtst line")
    print("10" + 10) # error 
except IOError:
    print("io에러가 발생하였습니다.")
except TypeError: # python docs에서 에러 참조 
    print("타입 에러 발생")
finally:
    print("Finally line")

# 두 값, a와 b를 받아들이고, a / b의 결과를 반환하는 divider(a,b)라는 함수를 작성하세요. 
# b가 0일 때, Python은 예외를 던집니다. 
# 이 ZeroDivisionError가 발생하면, "Please do not divide by zero!"를 출력하는 오류 처리 루틴을 작성하세요.
def divider(a, b):
    try: 
        return a / b 
    except ZeroDivisionError:
        print("Please do not divide by zero!")

divider(10, 0)