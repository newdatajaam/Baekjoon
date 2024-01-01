scene = 1
while True:
  o,w = map(int,input().split())
  if o == 0 and w == 0:
    break

  while True:
    state, kg = input().split()

    if state == '#':
      break
    elif state == 'E' and w > 0:
      w -= int(kg)
    elif state == 'F' and w > 0:
      w += int(kg)


  if o * 2 > w and w > o * 0.5:
    print(f"{scene} :-)")
  elif w <= 0:
    print(f"{scene} RIP")
  else:
    print(f"{scene} :-(")

  scene += 1