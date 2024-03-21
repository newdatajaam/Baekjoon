n, m = map(int,input().split())
board = []
min_cnt = 64

for _ in range(n): # n
  board.append(list(input())) # input()

# 1. n*m에 대하여 8*8로 반복하여 자르기
for i in range(n-7): # 0 1 2
  for j in range(m-7): # 0 1 2
    #print('print i ', i, 'print j ', j)
    chess_board = []
    for k in range(i,i+8):      
      chess_board.append(board[k][j:j+8])
    #print(chess_board)
    case1_cnt_W = 32
    case1_cnt_B = 32
    case2_cnt_W = 32
    case2_cnt_B = 32
    for row in range(8):
      for col in range(8):
        check = chess_board[row][col] # 체크판 확인하기
        
        if ((row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1)) :
          # 체스판이 W로 시작할 경우
          if check == 'W':
            case1_cnt_W -= 1
          # 체스판이 B로 시작할 경우
          else:
            case2_cnt_B -= 1
        elif ((row % 2 == 0 and col % 2 == 1)  or (row % 2 == 1 and col % 2 == 0)) :
          if check == 'B':
            case1_cnt_B -= 1
          else:
            case2_cnt_W -= 1
    #print(case1_cnt_W, case1_cnt_B)
    #print(case2_cnt_B, case2_cnt_W)
    #print(min(case1_cnt_W+case1_cnt_B, case2_cnt_W+case2_cnt_B))
    min_cnt = min(min_cnt, min(case1_cnt_W+case1_cnt_B, case2_cnt_W+case2_cnt_B))
print(min_cnt)