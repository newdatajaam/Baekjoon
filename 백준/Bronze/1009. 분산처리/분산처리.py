num_list = [[1,1,1,1],[2,4,8,6],[3,9,7,1],[4,6,4,6],[5,5,5,5],[6,6,6,6],[7,9,3,1],[8,4,2,6],[9,1,9,1]]

test = int(input())

for i in range(test):
  a,b = map(int,input().split())

  if a % 10 == 0:
    a = 10
  else:
    a = a%10

  if b%4 == 0:
    b = 4
  else:
    b = b%4
  
  if a == 10:
    print(10)
  else:
    print(num_list[a-1][b-1])