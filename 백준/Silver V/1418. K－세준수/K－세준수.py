num = int(input())
k = int(input())

def k_SejunNum(n): 
    i = 2
    while i <= n:
      if i > k:
         return 0
      if n % i == 0:
         n = n / i
         if n == 1:
            return 1
      else:
         i = i + 1


cnt = 0
for N in range(2, num+1): # 문제 오류인듯 소수를 1부터 카운트해야 일치
 if k_SejunNum(N):
  cnt += 1
print(cnt+1)