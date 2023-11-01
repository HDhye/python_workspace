# 딕셔너리: 키-쌍 값 
# 시퀀스와 순서가 중요하다면 딕셔너리보단 리스트를 사용한다.  

cabinet = {3:'kim', 100:'lee', "a-1":'yu'}

# get[key]
print(cabinet[3]) # kim 
print(cabinet.get(3)) # kim 

# print(cabinet[5]) #KeyError : 5
print(cabinet.get(5)) # None

# get(key, default) : 없으면 디폴트값 출력 
print(cabinet.get(5, '사용 가능')) # 사용 가능 

# int : key 존재유무 검사 
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

### 

employees = {"chef":"Amy", "ceo":"Jason"}
print(employees['ceo'])
# 새 키-값 쌍 추가하기 
employees["waiter"] = "Mike"
print(employees)
# 업데이트 K-V
employees["chef"] = "Jose"

stock_price = {"google":[200, 210, 220], "GME":[20, 100, 300]}
history = stock_price['google']
# first day price is : 200
print(f"first day price is : {history[0]}")

mydict = {"outer":{"inner": 100}}
# 100 
print(mydict["outer"]["inner"])

# 아래 정의된 딕셔너리에 키-값 쌍으로 "key4", 400을 추가한 다음, 업데이트된 딕셔너리의 모든 키-값 쌍을 출력하세요.
my_dict = {"key1": 100, "key2": 200, "key3": 300}
my_dict["key4"] = 400
print(my_dict.items())