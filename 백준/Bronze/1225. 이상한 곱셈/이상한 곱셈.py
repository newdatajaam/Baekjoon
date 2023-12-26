num1, num2 = input().split()

list1 = list(map(int,num1))
list2 = list(map(int,num2))

sum1 = 0
sum2 = 0

for i in list1:
  sum1+=i

for j in list2:
  sum2+=j

print(sum1*sum2)