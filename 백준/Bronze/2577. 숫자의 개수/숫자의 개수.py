# 2577
a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
answer = [0]*10
for i in result:
  answer[int(i)] += 1

for j in answer:
  print(j)