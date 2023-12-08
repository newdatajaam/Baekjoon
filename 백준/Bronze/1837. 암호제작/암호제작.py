num,k = map(int,input().split())
cnt = 2

for sosu in range(2,k): # 소수를 찾으려면 2 이상이어야 함
  # num안에 k보다 작은 소수가 있다면
  if num%sosu == 0:
    p = sosu
    # 2부터 for문이 돌기 때문에 p는 무조건 q보다 작은 숫자이기때문에
    print("BAD", p)
    break
  # num이 k 보다 작은 소수가 없다면
  else:
    cnt += 1

# k(=cnt)번 만큼 돌았는데도 소수가 없다면 k보다 큰 소수 인 것이므로 good출력
if cnt == k:
  print("GOOD")