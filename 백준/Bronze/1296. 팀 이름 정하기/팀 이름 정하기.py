
yeondoo = input()
team_num = int(input())
name_list = []
percent_list = []

max_p = 0
max_name = ''
for _ in range(team_num):
  name_list.append(input())

name_list = sorted(name_list)

for name in name_list:
  teamname = name + yeondoo

  l = teamname.count("L")
  o = teamname.count("O")
  v = teamname.count("V")
  e = teamname.count("E")

  ans = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100

  if ans == 0:
    pass
  elif ans > max_p :
    max_p = ans
    max_name = name

if max_p == 0:
  print(name_list[0])
else:
  print(max_name)