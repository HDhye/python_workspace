# list [] 

subway = [10, 20, 30]

sub1 = 10
sub2 = 20
sub3 = 30

subway2 = [sub1, sub2, sub3]

print(subway)
print(subway2)

# index
print(subway.index(20)) # 1 

# append : 맨 뒤에 추가
print(subway.append('haha'))
print(subway)   # [10, 20, 30, 'haha']

# insert : 특정 인덱스에 추가 
print(subway.insert(2, 'anna'))
print(subway)   # [10, 20, 'anna', 30, 'haha']

# pop : 기본은 맨 마지막, 혹은 특정 인덱스 뽑기
print(subway.pop(1)) # 20 
print(subway.pop(-1)) # haha
print(subway.pop(1)) # anna   --- 빼버리면 끝 

print(subway) # 10, 30 
print(subway.pop()) # 30 

subway.append(30)
subway.append(10)
print(subway) # [10, 30, 10] -- 중복 가능 
subway.append(5)

# sort : 정렬 
subway.sort()
print(subway)

# reverse
subway.reverse()
print(subway)

subway.append('hahahaha')
subway.append(True)
# subway.sort() # error 
print(subway)

# extend
subway.extend(subway2) 
print(subway) # [30, 10, 10, 5, 'hahahaha', True, 10, 20, 30]

# clear
subway.clear()
print(subway) # []

myvar = "NEW"
mylist = [100,200,300, 400, 500]

print(mylist)

# append : 맨 뒤에 추가하기
mylist.append(myvar)
# [100, 200, 300, 400, 500, 'NEW']
print(mylist)

# insert : 특정 인덱스에 삽입하기 
mylist.insert(1, myvar)
# [100, 'NEW', 200, 300, 400, 500, 'NEW']
print(mylist)



# 아래에 정의된 리스트를 정렬하고, 정렬된 리스트의 처음 세 요소를 출력하세요.
unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
unsorted_list.sort()
print(unsorted_list[0:3])
