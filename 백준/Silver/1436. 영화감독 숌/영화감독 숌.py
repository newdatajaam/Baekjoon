idx_loc = int(input())
end = '666'
end_list2 = []
cnt = 1

for t in range(10):
  for k in range(10):
    for j in range(10):
      for i in range(10):
        t = str(t)
        k = str(k)
        i = str(i)
        j = str(j)

        num1 = int(t + k + j + i + end)
        num2 = int(t + k + j + end + i)
        num3 = int(t + k + end + j + i)
        num4 = int(t + end + k + j + i)
        num5 = int(end + t + k + j + i)
        end_list2.extend([num1, num2, num3, num4, num5])

        cnt += 1
        

      if cnt >= idx_loc:
          break
    if cnt >= idx_loc:
          break
  if cnt >= idx_loc:
          break
print(sorted(set(end_list2))[idx_loc-1])