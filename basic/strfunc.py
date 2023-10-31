# 문자열 함수 

python = "Python is Amazing"

print(python.lower()) # python is amazing 
print(python.upper()) # PYTHON IS AMAZING

print(python[0].isupper()) # true 

print(len(python)) # 17 
print(python.replace("Python", "Java")) # Java is Amazing

print(python.index("n"))  # 5

index = python.index("n")
print(python.index("n", index + 1)) # 15 두번째 n 

print(python.find("n")) # 5 
print(python.find("java")) # -1 
# print(python.index("java")) # error  

print(python.count("n")) # 2 번 등장 




