train = 0
people = []

for station in range(0,4):
  get_out, get_in = map(int, input().split())
  train -= get_out
  if train < 0:
    print("오류")
  train += get_in
  if train > 10000:
    print("정원초과")
  people.append(train)

print(max(people))