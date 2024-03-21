n = int(input())
ans = []

for _ in range(n):
  word = input()
  while True:
    if len(word) == 0:
      break
    if '()' in word:
      word = word.replace('()','')
    else:
      break

  if len(word) == 0:
    ans.append("YES")
  else:
    ans.append("NO")

for x in ans:
  print(x)