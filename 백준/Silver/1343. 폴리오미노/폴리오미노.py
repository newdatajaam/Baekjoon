board = input().split('.')
polyomino = ''
ans = 1
for idx, letter_x in enumerate(board):
  length = len(letter_x)
  if letter_x == '':
    pass
  elif length % 2 == 0:
    
    while length // 4 > 0:
      if length // 4 > 0:
        polyomino += 'AAAA'
        length -= 4
    while length > 0:
      if length // 2 > 0:
        polyomino += 'BB'
        length -= 2
  else:
    ans = 0
    break
  polyomino += '.'

if ans:
  polyomino = polyomino[:-1]
  print(polyomino)
else: 
  print(-1)