num1,num2 = input().split()

num1 = int(str(num1),2)
num2 = int(str(num2),2)

sum = num1+num2
print(bin(sum)[2:])