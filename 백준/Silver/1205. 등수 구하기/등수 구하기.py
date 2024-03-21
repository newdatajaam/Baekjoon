N, new_score, p = map(int, input().split())

if N == 0: 
  print(1)
else:      
  score = list(map(int, input().split()))
  if len(score) == p and score[-1] >= new_score:
    print(-1)
  elif score[-1] >= new_score:  
      score.append(new_score)
      print(score.index(new_score)+1) 
  else:
    for i in range(len(score)): 
      if new_score >= score[i]:
        score.insert(i, new_score)
        score = score[:p]
        print(i+1)
        break
