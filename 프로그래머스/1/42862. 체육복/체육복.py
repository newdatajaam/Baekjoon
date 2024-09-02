def solution(n, lost, reserve):
    student = [1 for i in range(n)]

    lost.sort()
    
    for r in reserve:
        student[r-1] += 1
    
    for l in lost:
        student[l-1] -= 1
        
    for i in lost:
        if student[i-1] == 0:
            if i-1 > 0 and student[i-2] > 1:
                student[i-2] -= 1
                student[i-1] += 1
            elif i+1 <= n and student[i] > 1:
                student[i] -= 1
                student[i-1] += 1
    
    answer = n - student.count(0)
    
    return answer