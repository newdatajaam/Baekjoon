n = int(input())
bed = []
cnt_col,cnt_row = 0, 0
chk_list = []

for _ in range(n):
  bed.append(list(input()))

def cnt_def(list_name):
  cnt = 0
  if len(list_name) == 0:
    pass
  elif len(list_name) == 1: 
    cnt +=1
  else:
    cnt += 1
    for num in range(len(list_name)-1):
      if list_name[num]+1 != list_name[num+1]:
        cnt +=1
  return cnt

for i in range(n):
  for j in range(n-1):
    if bed[i][j] == '.' and bed[i][j] == bed[i][j+1]:
      chk_list.append(j)
  cnt_row += cnt_def(chk_list)
  chk_list = []

for j in range(n):
  for i in range(n-1):
    if bed[i][j] == '.' and bed[i][j] == bed[i+1][j]:
      chk_list.append(i)
  cnt_col += cnt_def(chk_list)
  chk_list = []
  
print(cnt_row, cnt_col)