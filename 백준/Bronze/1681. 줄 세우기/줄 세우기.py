# 1681번

n, l = map(int,input().split())
cnt = 1 # n과 동일해지는지 카운트하기
num = 1 # 1부터 하나씩 세기
last_num = 0

while True:
  if cnt > n:
    break
  if str(l) not in str(num):
    cnt += 1 
  num += 1

print(num-1)