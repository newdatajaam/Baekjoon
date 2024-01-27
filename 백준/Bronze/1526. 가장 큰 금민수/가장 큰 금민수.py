n = int(input())

while True:
  n_list = list(str(n))
  if len(n_list)== n_list.count('4')+ n_list.count('7'):
    print(n)
    break
  n -= 1