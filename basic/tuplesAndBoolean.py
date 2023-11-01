# 튜플 () : 리스트와 같은 시퀀스이지만, 불변성으로 인해 변경할 수 없다. 
# 아이템 순서의 변경을 기대하지 않거나 원하지 않을때 사용된다. 

# k-v도 튜플 

mylist = [1, 2, 3]
mytuple = (1, 2, 3)

mylist[0] = "New"
print(mylist) # ['New', 2, 3]
# mytuple[0] - "New" # error 변경을 허용하지 않음. 인덱싱은 존재함 
print(mytuple)  # (1, 2, 3)
print(mytuple[0]) # 1

# Booelan 
a = True 
b = False

# 값(1, 2, 3, 4, 5)을 가진 my_tuple이라는 튜플을 정의한 다음, my_tuple의 마지막 요소가 10보다 작은지 
# 그 여부를 출력하는 print 문을 작성하세요. 이 print함수의 내부는 부울린 값을 반환하는 간단한 비교 연산자로 작성되어야 합니다. (예: x <3)
my_tuple = (1,2,3,4,5)
print(my_tuple[-1] < 10 )


