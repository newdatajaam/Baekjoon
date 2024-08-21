# 26170
board = []
for _ in range(5):
  board.append(list(map(int, input().split())))

r, c = map(int, input().split())

apple = move = 0
answer = []

x = [1,-1,0,0]
y = [0,0,1,-1]

def dfs(board, r, c, move):
  global apple
  # print(r, c, apple)
  if apple == 3:
    # print(f'{move}번 움직임')
    answer.append(move)

  for i in range(4):
    nx = r + x[i]
    ny = c + y[i]

    if (0 <= nx < 5) and (0 <= ny < 5) and (board[nx][ny] != -1):
        if board[nx][ny] == 1:
          apple += 1

        temp = board[r][c]
        board[r][c] = -1
        dfs(board, nx, ny, move+1)
        board[r][c] = temp

        if board[nx][ny] == 1:
          apple -= 1

  return answer

if dfs(board, r,c, move):
  print(min(answer))
else:
  print(-1)