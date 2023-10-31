import sys 


N = int(input())
A = list(map(int, input().split()))
S = [0] * N

# Insertion Sort
for i in range(1, N):
    insert_value = A[i]
    j = i - 1
    while j >= 0 and A[j] > insert_value:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

total_sum = 0
for i in range(0, N):
    total_sum += S[i]



print("sum", total_sum)