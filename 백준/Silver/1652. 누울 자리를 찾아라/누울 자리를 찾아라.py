n = int(input())
bed = []
cnt_col = 0
cnt_row = 0
chk_list = []

for _ in range(n):
  bed.append(list(input()))

for i in range(n):
  for j in range(n-1):
    if bed[i][j] == '.' and bed[i][j] == bed[i][j+1]:
      chk_list.append(j)

  if len(chk_list) == 0:
    pass
  elif len(chk_list) == 1: 
    cnt_row +=1
  else:
    cnt_row += 1
    for num in range(len(chk_list)-1):
      if chk_list[num]+1 != chk_list[num+1]:
        cnt_row +=1
        #print(cnt_row)
  #print('*'*30)
  chk_list = []

for j in range(n):
  for i in range(n-1):
    if bed[i][j] == '.' and bed[i][j] == bed[i+1][j]:
      chk_list.append(i)
  
  #print(chk_list)
  if len(chk_list) == 0:
    pass
  elif len(chk_list) == 1: 
    cnt_col +=1
  else:
    cnt_col += 1
    for num in range(len(chk_list)-1):
      if chk_list[num]+1 != chk_list[num+1]:
        cnt_col +=1
  chk_list = []
  
print(cnt_row, cnt_col)