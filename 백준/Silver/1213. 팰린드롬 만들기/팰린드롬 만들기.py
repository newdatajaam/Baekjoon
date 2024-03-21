string = input()
pel_dict = {}
cnt = 0
odd_string = ''
ans = ''

for i in string:
  if i in pel_dict:
    pel_dict[i] += 1
  else:
    pel_dict[i] = 1

for j in pel_dict.values():
  if j % 2 == 1:
    cnt += 1

if cnt > 1:
  print("I'm Sorry Hansoo")
else: 
  pel_list = sorted(pel_dict.items(), key=lambda x: x[0])
  for key, value in pel_list:
    if value % 2 == 1:
      odd_string = key
      ans += key * (value//2)
    else:
      ans += key * (value//2)
  
  print(ans + odd_string + ans[::-1])
