# 1026번 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 내림차순
B.sort(reverse=True) # 오름차순

sum = 0
for i in range(N):
  sum += A[i] * B[i]

print(sum)