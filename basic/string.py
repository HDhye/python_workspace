print("hello")
myvar = "hello"

# upper case 
print(myvar.upper())

# lower case
print(myvar.lower())

# 첫번째 글자 대문자 
print(myvar.capitalize())

myvar2 = "Hello mike how is your dog"

# ['Hello', 'mike', 'how', 'is', 'your', 'dog']
print(myvar2.split())

# ['Hell', ' mike h', 'w is y', 'ur d', 'g']
print(myvar2.split("o"))

# Hello 
print(myvar2[0:5])

# MIKE
print(myvar2.split()[1].upper())

# Hello mike how is your do
print(myvar2[0:-1])

first_name = "Jose"
last_name = "Peter"

# f
# Hello Jose Peter
print(f"Hello {first_name} {last_name}")





