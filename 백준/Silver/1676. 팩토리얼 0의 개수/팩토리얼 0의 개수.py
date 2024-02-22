factorial = int(input())
num = 1
for i in range(1, factorial+1):
  num *= i

num = str(num)
n = -1
cnt = 0
while True:
  if num[n] == '0':
    cnt +=1
    n = n-1
  else:
    break
print(cnt)