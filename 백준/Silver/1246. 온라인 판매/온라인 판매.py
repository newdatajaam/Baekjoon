# 1246번 온라인 판매
# 31120kb	168ms
N, M = map(int, input().split())
price_list = []
revenue = []

for i in range(M): # 고객 M명의 가격 P(i)
  price_list.append(int(input()))


for j in range(len(price_list)):  # price = P(i) = A 로 설정
  cnt = 0
  price = price_list[j]

  for k in range(len(price_list)): # price = A일 때, 구매 고객 수 cnt
    if price_list[k] >= price:
      cnt += 1
      if cnt == N:  # 구매 고객 수(= 달걀 수)가 N명(개)이 되면 종료
        break
  revenue.append(price*cnt) # 수익 리스트

print(price_list[revenue.index(max(revenue))], max(revenue)) # (최대 수익의 가격, 최대 수익) 출력