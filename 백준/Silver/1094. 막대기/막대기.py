X = int(input())
sticks = [64]

while sum(sticks) > X:
  min_stick = min(sticks) /2
  sticks.remove(min(sticks))
  if sum(sticks) + min_stick >= X:
    sticks.append(int(min_stick))
    if sum(sticks) + min_stick == X:
      break
  else:
    sticks.append(int(min_stick))
    sticks.append(int(min_stick))
  
print(len(sticks))