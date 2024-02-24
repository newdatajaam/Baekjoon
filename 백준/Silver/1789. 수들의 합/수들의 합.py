S = int(input())
sum =0

i =1
while True:
  sum += i
  if S >= sum:
    i +=1
  else:
    break
print(i-1)