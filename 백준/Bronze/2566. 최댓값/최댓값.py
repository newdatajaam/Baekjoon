row = []
row_max = 0
row_count = 0
column_count = 0
column_max = 0

# 1열 부터 9열 반복 (편의상 1부터 10으로)
for i in range(1,10):
  row = list(map(int, input().split()))

  if max(row) >= row_max:
    row_max = max(row)
    row_count = i

    for num in row:
      column_count += 1
      if row_max == num:
        column_max = column_count
  column_count = 0

print(row_max)
print(row_count, column_max)