ddang = int(input())

for i in range(ddang):
  size, *soldiers = map(int, input().split())
  sold_dict = {}
  for j in soldiers:
    if j not in sold_dict:
      sold_dict[j] = 1
    else:
      sold_dict[j] += 1
  for key, value in sold_dict.items(): 
    if value > size//2:
      print(key)
      break
  else:
    print("SYJKGW")