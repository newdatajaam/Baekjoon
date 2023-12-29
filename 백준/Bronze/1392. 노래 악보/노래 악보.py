n, q = map(int, input().split())
time_list = []
time_sum = 0
akbo = []
i = 1

for _ in range(n):
  playtime = int(input())
  time_list.append(playtime) # [2,1,3]
  time_sum += playtime  # 총 6초


for time in time_list:
  for _ in range(time):
    akbo.append(i)  # [1,1,2,3,3,3]
  i = i+1

q_list =[]
for j in range(q):
  q_list.append(int(input())) # [2,3,4,0,1]

for a in q_list:
  print(akbo[a])