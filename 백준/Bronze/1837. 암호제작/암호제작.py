num,k = map(int,input().split())
cnt = 2

for sosu in range(2,k):
  # num안에 k보다 작은 소수가 있다면
  if num%sosu == 0:
    p = sosu
    q = int(num / p)
    # 2부터 for문이 돌기 때문에 p는 무조건 q보다 작은 숫자이기때문에
    print("BAD", p)
    break
  # num이 k 보다 작은 소수가 없다면
  else:
    cnt += 1

# k(=cnt)번 만큼 
if cnt == k:
  print("GOOD")