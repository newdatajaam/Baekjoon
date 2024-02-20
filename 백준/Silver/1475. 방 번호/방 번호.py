room_num = input()
plastic_set = [0]*10 

for i in room_num:
  plastic_set[int(i)] = room_num.count(i)

plastic_set[6] += plastic_set.pop(9)
plastic_set[6] = int(plastic_set[6]/2+0.5)
print(max(plastic_set))