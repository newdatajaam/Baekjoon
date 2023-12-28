# 1297번 TV크기

# (w * x)^2 + (h * x)^2 = d^2
# x^2 = d^2 / (w^2 + h^2)

d, h, w = map(int, input().split())
x = d/((h**2 + w**2)**0.5)

print(int(x*h),int(x*w))