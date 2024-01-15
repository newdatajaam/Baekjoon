trophy_num = int(input())
trophy_list = []
height = 0
l_cnt = 0
r_cnt = 0


for i in range(trophy_num):
  trophy_list.append(int(input()))

for trophy in trophy_list:
  if trophy > height:
    height = trophy
    l_cnt += 1

trophy_list.reverse()
height = 0

for trophy in trophy_list:
  if trophy > height:
    height = trophy
    r_cnt += 1

print(l_cnt)
print(r_cnt)