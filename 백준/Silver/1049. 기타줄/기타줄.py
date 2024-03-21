# 1049번 기타줄
N, M = map(int, input().split())
brand = []
for i in range(M):
  brand.append(list(map(int, input().split())))

all_pack = N // 6 +1
package = N // 6
leftover = N % 6

all_pack_price = []
each_price = []
pack_price = []
pack_leftover_price = []

for price in brand:
  all_pack_price.append(price[0] * all_pack)
  pack_price.append(price[0] * package)
  pack_leftover_price.append(price[1] * leftover)
  each_price.append(price[1] * N)

# print(all_pack_price)
# print(min(pack_price)+min(each_price))

print(min(min(all_pack_price),min(pack_price)+min(pack_leftover_price),min(each_price)))