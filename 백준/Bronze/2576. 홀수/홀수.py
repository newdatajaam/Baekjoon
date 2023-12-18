num_list = []   #자연수 입력받을 변수
odd_num = []    #홀수 입력받을 변수
odd_total = 0       #홀수들의 합

# 7번 자연수 입력받기
for nums in range(7):
  num_list.append(int(input()))

# 홀수 인지 확인하고 새 리스트 만들기
for number in num_list:
  if number % 2 == 1:
    odd_num.append(number)

# 홀수들의 합
for i in odd_num:
  odd_total+= i

# 출력
if len(odd_num) == 0:     # 홀수가 없는 경우 '-1'출력
  print(-1)
else:
  print(odd_total)        # 홀수가 있다면 '홀수들의 합'과 '홀수 최소값'을 출력
  print(min(odd_num))