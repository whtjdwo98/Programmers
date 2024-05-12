def solution(progresses, speeds):
    answer = []
    develop = 0
    while 1:
        if not progresses :return answer
        if progresses and progresses[0] < 100:
            progresses = [x+y for x,y in zip(progresses, speeds)]
            
        if progresses[0] >= 100:
            develop += 1
            progresses.pop(0)
            speeds.pop(0)
        if (not progresses or progresses[0] < 100) and develop > 0:
            answer.append(develop)
            develop = 0