cabinet = {3:'kim', 100:'lee', "a-1":'yu'}

# [key]
print(cabinet[3]) 
print(cabinet.get(3)) # kim 

# print(cabinet[5]) #KeyError : 5
print(cabinet.get(5)) # None
print(cabinet.get(5, '사용 가능')) # 사용 가능 

print(3 in cabinet) # true 
print('a-1' in cabinet) # true 

# 할당 
cabinet["c-1"] = 'pakr'
print(cabinet)  # {3: 'kim', 100: 'lee', 'a-1': 'yu', 'c-1': 'pakr'}
# 재할당
cabinet["a-1"] = 'yooooo'
print(cabinet)  # {3: 'kim', 100: 'lee', 'a-1': 'yooooo', 'c-1': 'pakr'}

# delete 
del cabinet['a-1']

# key - value 
print(cabinet.keys())   # dict_keys([3, 100, 'c-1'])
print(cabinet.values()) # dict_values(['kim', 'lee'])
print(cabinet.items())  # dict_items([(3, 'kim'), (100, 'lee'), ('c-1', 'pakr')])

# clear
cabinet.clear()
print(cabinet) #{}