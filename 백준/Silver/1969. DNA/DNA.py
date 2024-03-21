# 1969 DNA
N, M = map(int, input().split())
dna = [[] for _ in range(M)]
total = 0
ans = ''

for i in range(N):
  temp1 = list(input()) 
  for j in range(M):
    dna[j].append(temp1[j])
# print(dna)

for col in dna:
  set_col = list(set(col))
  temp_list = []
  for abc in set_col:
    abc_cnt = col.count(abc)
    temp_list.append([abc, abc_cnt])

  if len(temp_list) == 1:
    # print(temp_list[0][0], 'len 1')
    ans += temp_list[0][0]
  else:
    temp_list.sort(key=lambda x:[-int(x[1]), x[0]])
    # print(temp_list)
    # print(temp_list[0][0])
    # print(temp_list[0][1], '값')
    ans += temp_list[0][0]
    total += (N - int(temp_list[0][1]))

print(ans)
print(total)