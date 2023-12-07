num1, num2 = map(int,input().split())

horizontal = 0
vertical = 0

if num1%4 == 0 and num2%4 != 0:
  horizontal = abs(((num1)//4-1) - (num2)//4)
  vertical = abs(((num1)%4+4) - (num2)%4)
elif num2%4 == 0 and num1%4 != 0:
  horizontal = abs((num1)//4 - ((num2)//4-1))
  vertical = abs((num1)%4 - ((num2)%4+4))
else:
  horizontal = abs((num1)//4 - (num2)//4)
  vertical = abs((num1)%4 - (num2)%4)

total = horizontal + vertical
print(total)