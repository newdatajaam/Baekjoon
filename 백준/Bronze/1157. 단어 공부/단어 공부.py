word = list(input().upper())
abc_list = {}
answer = ''

for abc in word:
  if abc in abc_list:
    abc_list[abc] += 1
  else:
    abc_list[abc] = 1

max_num = max(abc_list.values())

for key, value in abc_list.items():
  if value == max_num:
    answer += key

if len(answer) > 1 :
  print('?')
else:
  print(answer)