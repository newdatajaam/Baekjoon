
number = input()
kijun = 1
i = 0
while i < len(number):
  temp = str(kijun)
  for j in range(len(temp)):
    if i >= len(number):
      break
    if temp[j] == number[i]:
      i += 1
  kijun +=1
print(kijun-1)