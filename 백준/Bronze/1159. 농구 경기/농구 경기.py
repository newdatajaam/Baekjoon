player_num = int(input())
player_list = []
answer = ''

for _ in range(player_num):
  name = input()
  player_list.append(name[0])

temp_list = sorted(set(player_list))

for apb in temp_list:
  if player_list.count(apb) >= 5:
    answer += apb
    
  
if len(answer) == 0:
  print("PREDAJA")
else:
  print(answer)