while True:
  a, *aa = map(int,input().split())
  branch = 1

  if a == 0:
    break

  for i in range(0,len(aa)):
    # aa 인덱스의 홀수 번째[0,2,4...번째] - 가지 성장
    if i%2 == 0:
      branch = branch * aa[i]
    # aa 인덱스의 짝수 번째[1,3,5...번째] - 가지치기
    elif i%2 == 1:
      branch = branch - aa[i]

  print(branch)