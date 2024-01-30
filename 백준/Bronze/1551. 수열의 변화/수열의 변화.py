n, k = map(int,input().split())
a = list(map(int,input().split(','))) # , 로 바꿔줘야함

def print_answer(x):
  ans = ''
  for i in x:
    ans += str(i)+','
  ans = ans.rstrip(',')
  print(ans, end='')

if k == 0:
  print_answer(a)
else:
  for i in range(k):
    b = []
    for num in range(len(a)-1):
      b.append(a[num+1]-a[num])
    a = b
  print_answer(b)