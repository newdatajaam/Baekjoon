def solution(s):
    n = len(s)
    answer = n

    for unit in range(1, n//2+1):
        cnt = 1
        now = s[:unit]
        temp_answer = ''

        for i in range(unit, n+unit, unit):
            # case1) 스캔 반복
            if s[i:i+unit] == now:
                cnt += 1
            # case2) 반복 중단 
            # 2-1) 압축이 되는 경우
            else:   
                if cnt > 1:
                    temp_answer+=str(cnt)+now
                else: 
                    temp_answer += now
                # 2 정리) 초기화
                now = s[i:i+unit]
                cnt = 1
        answer = min(answer, len(temp_answer))
        
    return answer

solution('aabbaccc')