#2455번 지능형 기차

train = 0
people = []

for station in range(0,4):
  get_out, get_in = map(int, input().split())
  train -= get_out
  train += get_in
  people.append(train)

  if train > 10000:
    print("정원초과")
  elif train < 0:
    print("오류")
  
print(max(people))