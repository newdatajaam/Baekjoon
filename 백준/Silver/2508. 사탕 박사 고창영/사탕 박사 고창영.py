test = int(input())

for _ in range(test):
  input()
  board = []
  cnt = 0

  row, col = map(int, input().split())
  for _ in range(row):
    board.append(list(input()))
  
  for i in range(row-2):
    for j in range(col):
      if board[i][j] == 'v' and board[i+1][j] == 'o' and board[i+2][j] == '^':
        cnt += 1
  
  for i in range(row):
    for j in range(col-2):
      if board[i][j] == '>' and board[i][j+1] == 'o' and board[i][j+2] == '<':
        cnt += 1
      
  print(cnt)