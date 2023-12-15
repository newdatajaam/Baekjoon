test = int(input())

for i in range(test):
  a, b = map(int,input().split())
  if b % 4 == 0:
    b = 4
  else: 
    b = b % 4
  
  num = a**b
  
  if num % 10 == 0:
    print(10)
  else:
    print(num%10)