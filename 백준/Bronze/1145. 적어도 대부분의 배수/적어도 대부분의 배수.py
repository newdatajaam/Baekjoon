# 1145번
num_list = list(map(int,input().split()))
min_num = min(num_list)

while True:
  cnt = 0 
  for num in num_list:
    if min_num % num == 0:      # 최소값부터 시작해서 자연수의 배수가 몇개인지 카운트
      cnt += 1

  if cnt >= 3:                  # 만약 3개 이상이면 종료하고 출력
    break

  min_num += 1                  # 3개 이상 배수가 아니라면 다음 +1 최소값으로

print(min_num)