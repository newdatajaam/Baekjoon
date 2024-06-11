def solution(friends, gifts):
  gift_list = [[0]*len(friends) for _ in range(len(friends))] # 선물 주고 받은 횟수 저장
  gift_index = [[0]*3 for _ in range(len(friends))] # 선물 지수 저장
  predict = [0]*len(friends) # 다음달 선물 받을 사람 예측치(=결과)
  answer = 0

  for gift in gifts: # 선물 주고 받은 내역을 수치로 저장
    # friends 정보에 있는 위치값에 맞게 사람별로 선물 준 횟수를 저장
    giver, taker = gift.split()
    gift_list[friends.index(giver)][friends.index(taker)] += 1
    # 선물 지수 계산을 위해 총 준 횟수와 받은 횟수를 카운트
    gift_index[friends.index(giver)][0] += 1
    gift_index[friends.index(taker)][1] += 1
  
  # 선물 지수 계산을 위해 저장한 값을 통해 선물 지수 계산 
  for i in range(len(gift_index)): # 각 인물 별 [선물 준 횟수, 선물 받은 횟수, 선물 지수] 형태로 저장
    gift_index[i][2] = gift_index[i][0] - gift_index[i][1]

  for i in range(len(gift_list)):
    for j in range(len(gift_list)):
      if i == j:
        pass
      else:
        if gift_list[i][j] > gift_list[j][i]:
          predict[i] += 1
        elif gift_list[i][j] == gift_list[j][i]:
          if gift_index[i][2] > gift_index[j][2]:
            predict[i] += 1

  answer = max(predict)
  return answer