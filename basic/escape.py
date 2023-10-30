# 탈출 문자 

print("백문이 불여일견\n백견이 불여일타") # 줄바꿈 
print("저는 \"안나\"입니다")    # 문장내 따옴표 
print("저는 '안나'입니다")

# \r : 커서를 맨 앞으로 이동 
print("red apple \rpine") # pineapple 

# \b 백스페이스 (앞에 한글자 삭제) 
print('redd\bapple') #redapple 

# \t tab 
print('red\tapple')

url = "http://www.naver.com"
index1 = url.index(".")
print(index1)
index2 = url.index(".", index1+1)
print(index2)
domain = url[index1+1:index2]
print(domain)
print(domain[:3]+str(len(domain))+ str(domain.count("e"))+'!')