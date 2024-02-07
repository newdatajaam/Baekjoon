n = int(input())
ans = 0 

for i in range(n):
  word = list(input())
  flag = True
  checked_list = []

  for check in word:
    cnt = 0
    if check not in checked_list:
      if word.count(check) == 1:
        pass
      else:
        for idx in range(len(word)-1):
          if word[idx] == check and word[idx+1] == check:
            cnt +=1
        if cnt == (word.count(check) -1):
          
          pass
        else:
          flag = False
      checked_list.append(check)

  if flag:
    ans+=1

print(ans)