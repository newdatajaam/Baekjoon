# 1434번 책 정리

box, book = map(int,input().split())

box_list = list(map(int,input().split()))
book_list = list(map(int,input().split()))


for weight in book_list:
  i = 0
  while True:
    if box_list[i] < weight:
      i += 1
      pass
    else:                                  # box_list[i] >= weight
      box_list[i] -= weight
      break

answer = 0
for i in box_list:
  answer+= i

print(answer)