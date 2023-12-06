# 변수 입력 받기
call = int(input())
num_list = list(map(int, input().split()))

# 영식과 민식의 요금제 총합
y_plan = 0
m_plan = 0

for i in range(call):
  y_plan += ((num_list[i]//30)+1) * 10
  m_plan += ((num_list[i]//60)+1) * 15

if y_plan < m_plan:
  print("Y", y_plan)
elif y_plan == m_plan:
  print("Y","M", y_plan)
else:
  print("M", m_plan)