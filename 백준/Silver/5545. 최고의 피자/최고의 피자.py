num_topping = int(input())
dough_price, topping_price = map(int, input().split())
dough_kcal = int(input())
topping_kcal = [int(input()) for _ in range(num_topping)]
topping_kcal.sort(reverse=True)

best_kcal = int(dough_kcal / dough_price)
for num in range(1, num_topping+1):
  tot_price = dough_price + topping_price * num
  tot_kcal = dough_kcal + sum(topping_kcal[0:num])

  #print(num, tot_kcal, tot_price, best_kcal)

  if tot_kcal / tot_price > best_kcal:
    best_kcal = int(tot_kcal / tot_price)
print(best_kcal)