def solution(participant, completion):
    dict = {}
    answer =''
    
    for name in participant:
        if name in dict:
            dict[name] += 1 
        else:
            dict[name] = 1
            
    for name in completion:
        if dict[name] == 1:
	        del dict[name]
        else:
            dict[name] -= 1
    answer = list(dict.keys())[0]
    return answer
