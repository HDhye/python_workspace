# 문자열 포맷 

# 1. %
print("i am %d years old" % 20)
print("i am %s years old" % 20) # int -> str 
print("i like %s language" %'python')
print("Apple is start %c" %'A') 

print("--- %s ---- %s" % ('red', 'blue'))

# 2. 
print('i am {} years old' .format(20))
print("--- {} ---- {} " .format('red', 'blue')) # red, blue 
print("--- {1} ---- {0} " .format('red', 'blue')) # blue, red 

# 3. 
print("나는 {age} 살이며, {color}을 좋아해요. " .format(age = 20, color='빨간색'))

# 4. (v3.6 ~ )
age = 20 
color = 'blue'
print(f"나는 {age} 살이며, {color}을 좋아해요. ")
