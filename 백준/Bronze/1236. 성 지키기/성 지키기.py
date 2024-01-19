# 가로줄에 최소 1명씩 새로줄에 1명씩 카운트
row_num, column_num = map(int, input().split())
total_cols = []        # 세로줄
total_row = [0] * column_num # 가로줄

for _ in range(row_num):
  input_row = list(input())

  for i in range(len(input_row)):
    if input_row[i] == 'X':
      input_row[i] = 1
      # 최종 가로줄 지속 합산
      total_row[i] += 1
    else:
      input_row[i] = 0

  # 최종 세로줄 합산
  total_cols.append(sum(input_row))

row_no_guard = 0
col_no_guard = 0

# 최종 가로 줄의 경비병 수, 세로줄의 경비병 수를 기준으로 더 필요한 최소 경비병 수 구하기
for j in total_row:
  if j == 0:
    row_no_guard += 1

for k in total_cols:
  if k == 0:
    col_no_guard += 1

print(max(row_no_guard,col_no_guard))