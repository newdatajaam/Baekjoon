# 1100번 하얀칸
#

# 1.8*8칸을 입력받음
chess_board = []
cnt = 0

for i in range(8):
  chess_board.append(list(input()))

# 짝수줄 => 짝수가 하얀칸
# 해당칸에 'F'가 있으면 카운트 +1
for even_row in range(0,8,2):
  for even_column in range(0,8,2):
    if chess_board[even_row][even_column] == 'F':
      cnt += 1

# 홀수줄 => 홀수가 하얀칸
for odd_row in range(1,8,2):
  for odd_column in range(1,8,2):
    if chess_board[odd_row][odd_column] == 'F':
      cnt += 1

print(cnt)