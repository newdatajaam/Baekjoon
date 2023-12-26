n = input()

# 8진수 -> 10진수
n_to_ten = int(n, 8)

# 10진수 -> 2진수
# 맨 앞의'0b' 제외
print(bin(n_to_ten)[2:])