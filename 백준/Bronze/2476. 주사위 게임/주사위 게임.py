people = int(input())
all_price = []
for times in range(people):
  dice1, dice2, dice3 = map(int, input().split())

  if dice1 == dice2 == dice3:
    all_price.append(10000 + dice1 * 1000)
  elif dice1 == dice2 != dice3 or dice1 == dice3 != dice2 or dice2 == dice3 != dice1:
    all_price.append(1000+max(dice1,dice2)*100)
  elif dice1 != dice2 != dice3:
    all_price.append(max(dice1,dice2,dice3)*100)

print(max(all_price))