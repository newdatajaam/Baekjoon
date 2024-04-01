def solution(queue1, queue2):
    answer = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    else:
        target = (sum1 + sum2)//2

    if sum1 < sum2:
      total = queue1 + queue2 + queue1
    else:
      total = queue2 + queue1 + queue2

    
    start_pos = 0
    end_pos = len(queue1)
    sum_chk = sum(total[:end_pos])

    while True:
        if sum_chk == target:
            break
        elif (len(queue1) + len(queue2))+1< answer:
            answer = -1
            break        

        while sum_chk < target:
          sum_chk += total[end_pos]
          end_pos += 1
          answer += 1

        while sum_chk > target:
          sum_chk -= total[start_pos]
          start_pos += 1
          answer += 1
          
    return answer
