# 1453번 피시방 알바
people_num = int(input())
new_person = list(map(int,input().split()))
pc_num = [0]*100
rej = 0

for i in new_person:
  if pc_num[i-1] == 0:
    pc_num[i-1] = 1
  elif pc_num[i-1] == 1:
    rej += 1

print(rej)