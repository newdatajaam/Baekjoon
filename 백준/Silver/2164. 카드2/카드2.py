n = int(input())
card = [i for i in range(1,n+1)]

while len(card) > 1:
  if len(card) % 2 == 0: # 짝수라면
    card = card[1::2]
  else: # 홀수라면
    card = [card[-1]] + card[1::2]
print(card[0])