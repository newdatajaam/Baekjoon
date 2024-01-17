
file_num = int(input())
files = []

for _ in range(file_num):
  files.append(input())

answer = list(files[0])

for i in range(file_num-1):
  for j in range(len(files[0])):
    if files[i][j] == files[i+1][j] and answer[j] != '?':
      answer[j] = files[i][j]
    else:
      answer[j] = '?'

print(''.join(answer))