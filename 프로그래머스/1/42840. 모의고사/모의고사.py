def solution(answers):
    answer = []
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    
    for i in range(len(answers)):
        ans = answers[i]
        if ans == stu1[((i+1)%(len(stu1)))-1]:
            scores[0] += 1
        if ans == stu2[((i+1)%(len(stu2)))-1]:
            scores[1] += 1
        if ans == stu3[((i+1)%(len(stu3)))-1]:
            scores[2] += 1
    
    mx_sc = max(scores)
    for idx, j in enumerate(scores):
        if j == mx_sc:
            answer.append(idx+1)
    
    return answer

