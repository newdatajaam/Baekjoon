N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

ans = False
def dfs(row, col):
  global ans
  if maps[row][col] == -1:
      ans = True
      return
  nrow = row + maps[row][col]
  ncol = col + maps[row][col]
  if row == nrow and col == ncol:
    return
  if 0 < nrow < N and 0 < ncol < N:
    dfs(nrow, col)
    dfs(row, ncol)
  if 0 < nrow < N and ncol >= N :
    dfs(nrow, col)    
  if 0 < ncol < N and nrow >= N:
    dfs(row, ncol)
  return

dfs(0, 0)

if ans:
  print('HaruHaru')
else:
  print('Hing')