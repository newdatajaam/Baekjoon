idols, quiz = map(int, input().split())
girlgroup = {}

for _ in range(idols):
  group_name = input()
  members  = int(input())
  group_member = [] 
  for _ in range(members):
    group_member.append(input())
  
  girlgroup[group_name] = group_member

for i in range(quiz):
  q = input()
  cat = int(input())
  for key, value in girlgroup.items():
    if cat == 1:
      if q in value:
        print(key)
        break
    elif cat == 0:
      if q == key:
        value.sort()
        for name in value:
          print(name)
        break