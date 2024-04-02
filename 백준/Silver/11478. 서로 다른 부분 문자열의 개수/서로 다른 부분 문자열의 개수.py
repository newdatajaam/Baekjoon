string = input()
ans = []

for i in range(1, len(string)+1):
  for j in range(len(string)-i+1):
    ans.append(string[j:j+i])

print(len(set(ans)))