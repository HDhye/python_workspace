# 반복문 While Loops
n = 1  # Truthy
check = '' # Falsy 

while n < 5:
    print(f"현재 n값: {n}")
    n += 1

while n : # truthy값 조심
    print(n)
    n = check 

# 0에서 1000(1000 포함)의 값을 가지는 my_list라는 리스틀 만드는 루틴을 구현하세요.
my_list = []

m = 0
while m <= 1000:
    my_list.append(m)
    m += 1

