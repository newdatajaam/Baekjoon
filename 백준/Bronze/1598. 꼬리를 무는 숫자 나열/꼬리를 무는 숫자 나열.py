a, b = map(int, input().split())

dict = {a:((a-1)//4, (a-1)%4), b:((b-1)//4, (b-1)%4)}

x = abs(dict[a][0] - dict[b][0])
y = abs(dict[a][1] - dict[b][1])

print(x+y)