def solution(participant, completion):
    dict = {}
    calc = 0
    for i in range(0, len(completion)):
        dict[hash(participant[i])] = participant[i]
        calc = calc + hash(participant[i]) - hash(completion[i])
    dict[hash(participant[-1])] = participant[-1]
    calc += hash(participant[-1])
    
    return dict[calc]