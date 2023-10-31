# ranmdom 라이브러리 사용
from random import *

print(random())  # 0.0 ~ 1.0 미만 
print(random() * 10 + 1)
print(int(random() * 10) + 1)

# 1 ~ 46 미만 랜덤숫자 출력 
print(randrange(1, 46)) 
print(randrange(1, 46, 2)) # 홀수만 
print(randrange(2, 46, 2)) # 짝수만 





