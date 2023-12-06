x,y,w,h = map(int,input().split())

a= min(abs(x-0),abs(x-w),abs(y-0),abs(y-h))
print(a)