max_num = 0
column_count = 0
row_max = 0
column_max = 0

# 1열 부터 9열 반복 (편의상 1부터 10으로)
for i in range(1,10):
  row = list(map(int, input().split()))

  if max(row) >= max_num:
    max_num = max(row)
    row_max = i

    for num in row:
      column_count += 1
      if max_num == num:
        column_max = column_count
  column_count = 0

print(max_num)
print(row_max, column_max)