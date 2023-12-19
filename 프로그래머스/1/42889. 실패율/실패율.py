def solution(N, stages):
    answer = []
    result = []
    people = len(stages) # 도전자 수 
    cnt = 0 # 실패자 수 
    
    for n in range(1, N+1):
        cnt = stages.count(n)
    
        if people == 0:
            fail_rate = 0
            result.append([n, fail_rate])
        else:
            fail_rate = cnt / people
            people -= cnt   # 도전자 수 - 실패자 수
            result.append([n, fail_rate])
            cnt = 0 # 실패자 수 초기화
    temp = sorted(result, key = lambda x: (-x[1], x[0]))
    answer = [i[0] for i in temp]
    return answer