# 연산자 

print(2**3) # 2^3 = 8
print(5//3) # 몫 = 1 
print(10//3) # 3
 
print(10 > 3) #true

print(3 == 3) # true
print('str' == 'str') #true 

test1 = 'str'
test2 = 'str'

print(test1 == test2) # true 

print((3 > 0) and (3 < 5)) #true 
print((3 < 0) & (3 < 5)) # false
print((3 < 0) or (3 < 5) ) # true 
print((3 < 0) | (3 < 5)) # true  

print(2 + 3 * 4) # 14 
print((2+3) * 4 ) # 20 우선순위 연산 

number = 2 + 3 * 4

number += 2 
print(number) # 16 

#절대값 
print(abs(-5)) #5 
#제곱 
print(pow(4, 2)) # 16 
#최대값
print(max(5, 12)) # 12
#최소값
print(min(5, 12)) #5 
#반올림
print(round(3.14)) #3 

# math 라이브러리 사용
from math import *

#내림 
print(floor(4.99)) # 4 
#올림
print(ceil(3.14)) # 4
#제곱근 
print(sqrt(16)) # 4.0





