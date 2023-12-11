for times in range(0,3):
  yut = []
  add = 0

  yut = list(map(int,input().split()))

  for i in yut:
    add += i

  if add == 3:
    print("A")
  elif add == 2:
    print("B")
  elif add == 1:
    print("C")
  elif add == 0:
    print("D")
  elif add == 4:
    print("E")
