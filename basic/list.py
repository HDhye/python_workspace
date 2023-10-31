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

# append
print(subway.append('haha'))
print(subway)   # [10, 20, 30, 'haha']

# insert
print(subway.insert(2, 'anna'))
print(subway)   # [10, 20, 'anna', 30, 'haha']

# pop
print(subway.pop(1)) # 20 
print(subway.pop(-1)) # haha
print(subway.pop(1)) # anna   --- 빼버리면 끝 

subway.append(10)
print(subway) # [10, 30, 10] -- 중복 가능 
subway.append(5)

# sort 
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