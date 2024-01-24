x,y = map(str,input().split())

num = int(x[::-1]) + int(y[::-1])
num = str(num)

print(int(num[::-1]))