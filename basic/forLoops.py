# 제어문 for Loops 

# for in 
mylist = [1,2,3,4,5]
for item in mylist:
    print(item)
    # 1   
    # 2   
    # 3 
    # 4 
    # 5


# list뿐만 아니라 튜플이나 딕셔너리에도 가능하다. 

mytuple = (1,2,3,4,5)
for sales in mytuple:
    print(f"sale of : {sales}")

mydictionary = {'ceo':'andy', 'cfo': 'jane'}
for key in mydictionary:
    print(f"직급은 {key}, 그의 이름은 {mydictionary[key]}입니다")

# 다중 for문 
# 1 list, 3 tuples
mylist2 = [('a','b'), ('c','d'), (1,2)]

for item in mylist2:
    print(item)
    for i in item:
        print(i)
    # ('a', 'b')
    # a
    # b
    # ('c', 'd')
    # c
    # d
    # (1, 2)
    # 1
    # 2
    
# == 
for item1, item2 in mylist2:
    print(item1)
    print(item2)
# a
# b
# c
# d
# 1
# 2


# my_list1을 반복하는 for 루프를 작성하고, 루프 안에서 매번 값에 42를 추가하여, 
# 그 새로운 결과를 my_list2에 추가하세요. 아무것도 출력하지 않다도 됩니다. 
# mylist2 해답에 대해 여러분의 my_list2답을 확인하고자 합니다.
my_list1 = [1, 2, 3, 4, 5, 10]
my_list2 = []

for item in my_list1:
    my_list2.append(item + 42)

print(my_list2)