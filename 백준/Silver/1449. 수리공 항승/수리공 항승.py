n, l = map(int, input().split())
repair = list(map(int, input().split()))
repair.sort()

cnt = 0
distance = 0
for i in range(n-1):
  temp = (repair[i+1] - repair[i])
  if distance + temp >= l:
    cnt += 1
    distance = 0
  else:
    distance += temp
  #print(temp, distance, cnt)
    
print(cnt+1)