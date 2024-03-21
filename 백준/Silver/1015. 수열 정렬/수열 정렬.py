n = int(input())
A = list(map(int,input().split()))  

A_arr = []
for idx1, i in enumerate(A):
  A_arr.append([idx1, i])

A_arr.sort(key=lambda x:x[1])

B_arr = []
for idx2, j in enumerate(A_arr):
  B_arr.append(j + [idx2])

B_arr.sort(key=lambda x:x[0])

for x in B_arr:
  print(x[2], end=' ')