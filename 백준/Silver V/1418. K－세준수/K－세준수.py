num = int(input())
k = int(input())

def k_SejunNum(n): 
    i = 2
    while i <= n:
      if i > k:
         return 0   

      if n % i == 0:  
         n = n / i  
      else:
         i = i + 1  
         
    return 1

cnt = 0
for N in range(2, num+1):
 if k_SejunNum(N):
  cnt += 1
print(cnt+1)