# 2545번 팬케익 먹기
test = int(input())
ans = []
for _ in range(test):
  input()
  a, b, c, bite = list(map(int, input().split()))
  tot_size = a*b*c
  pancake = [a ,b, c]

  for _ in range(bite):
    pancake.sort(reverse=True)
    #print(pancake)
    pancake.append(pancake[0]-1)
    pancake.remove(pancake[0])
    #print(pancake, '과정', i)
    eat = pancake[0] * pancake[1]
    #print(eat, '먹기')
    tot_size -= eat
  ans.append(tot_size)
for x in ans:
  print(x)

# a,b,c 중에 최댓값을 뽑아내고
# 나머지 둘을 곱하고
# tot_sizes에서 빼주고
