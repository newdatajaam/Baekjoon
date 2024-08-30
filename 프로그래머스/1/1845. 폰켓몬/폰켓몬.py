def solution(nums):
    pokemons = {}
    answer = 0
    
    for i in nums:
        if i in pokemons:
            pokemons[i] += 1
        else:
            pokemons[i] = 1
    
    if len(pokemons) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(pokemons)
    
    return answer