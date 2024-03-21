# 26169번 세 번 이내에 사과를 먹자
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
x, y = map(int, input().split())
cnt = 0
move = 0
ans = False

# 왼 아래 오 위
nr = [0, 1, 0, -1]
nc = [-1, 0, 1, 0]

def dfs(row, col):
  global cnt, move, ans

  visited[row][col] = 1
  if move == 1:
    cnt = 0

  if move > 3:
    move -= 1
    return
  else:
    move += 1

  if board[row][col] == -1:
    return
  elif board[row][col] == 1 and cnt <= 2:
    cnt += 1

  if cnt >= 2:
    ans = True

  for i in range(4):            # 다음 위치 확인
    nrow = row + nr[i]
    ncol = col + nc[i]
    if 0 <= nrow < 5 and 0 <= ncol < 5 and move == 1:
        visited[nrow][ncol] = 0
    if 0 <= nrow < 5 and 0 <= ncol < 5 and visited[nrow][ncol] == 0 and move <= 3: # 이동 가능하면 이동
      dfs(nrow, ncol) 
      move -= 1
    else:
      continue
  return

dfs(x, y)

if ans:
  print(1)
else:
  print(0)