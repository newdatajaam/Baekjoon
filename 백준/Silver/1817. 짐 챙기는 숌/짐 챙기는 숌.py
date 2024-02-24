book_num, box_weight = map(int, input().split())
box = 0
weight = 0

if book_num == 0:
  print(box)
else:
  book_list = list(map(int, input().split()))
  for i in range(len(book_list)):
    weight += book_list[i]
    if weight > box_weight:
      box += 1
      weight = book_list[i]
    elif weight == box_weight:
      box += 1
      weight = 0
    else:
      pass

  if weight != 0:
    box += 1

  print(box)