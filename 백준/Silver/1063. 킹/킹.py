king, stone, move = input().split()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
movement = {'T': [0,1], 'B': [0,-1], 'R': [1,0], 'L': [-1,0],
            'RT': [1,1], 'LT': [-1,1], 'RB': [1,-1], 'LB': [-1,-1]}
for idx, a in enumerate(alphabet):
  if a == king[0]:
    king_x = idx+1
  if a == stone[0]:
    stone_x = idx+1

king_y = int(king[1])
stone_y = int(stone[1])

for i in range(int(move)):
  nx, ny = movement[input()]
  #print(nx,ny)
  if 1 <= king_x + nx <= 8 and 1 <= king_y + ny <= 8:
    if king_x + nx == stone_x and king_y + ny == stone_y:
      if 1 <= stone_x + nx <= 8 and 1 <= stone_y + ny <= 8:
        stone_x += nx
        stone_y += ny
        king_x += nx
        king_y += ny
      else:
        pass
    else:
      king_x += nx
      king_y += ny
  else:
    pass

print(alphabet[king_x-1]+str(king_y))
print(alphabet[stone_x-1]+str(stone_y))