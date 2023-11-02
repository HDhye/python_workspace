# 제어문 if elif else 

password = 'mypassword'
stored_pw = 'mypassworddddd'
admin = True

if password == stored_pw: 
    print('True!')
    print('passwords match!')
elif admin:
    print("password 오류, 그러나 관리자 권한입니다.")
else:
    print("password 오류")


# a와 b의 합이 42인지 확인하는 제어 흐름 루틴을 작성하세요. 합이 42이라면 42를 출력하세요. 
# 그렇지 않다면 합이 30과 41 사이인지 확인하고, a와b의 합을 출력하세요. 그것도 아니라면 False를 출력하세요.
a = 3
b = 8
sum = a+b 
if sum == 42:
    print(42)
elif sum >= 30 and sum <= 41:
    print(sum)
else:
    print(False)

