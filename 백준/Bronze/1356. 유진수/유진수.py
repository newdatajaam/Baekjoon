num = list(input())

ans = 0 

for i in range(len(num)-1):
  num_1,num_2 = 1,1
  
  for j in num[:i+1]: # i번까지
    num_1 *= int(j)
  for k in num[i+1:]: # i+1번 부터
    num_2 *= int(k)

  if num_1 == num_2:
    ans+= 1

if ans > 0:
  print("YES")
elif ans == 0:
  print("NO")