"""
1. 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리
2. 작업이 끝났을 때 요청들어온 작업들이 여러 개라면, 요청 시간 + 작업 시간이 작은 작업부터 처리
3. heapq는 첫 번째 요소를 기준으로 힙 구성
4. 작업완료시간이 작은 순서부터 수행할 경우 평균 시간 짧아짐
"""
import heapq as h
def solution(jobs):
    answer = 0
    time = 0
    stays = []
    h.heapify(jobs)
    h.heapify(stays)
    lenjobs = len(jobs)
    while 1:
        while 1:
            try:
                a = h.heappop(jobs)
            except:
                break
            if a[0] <= time:
                h.heappush(stays, [a[1], a[0]])
            else:
                h.heappush(jobs, a)
                break
        try:
            completetime = h.heappop(stays)
            
            if time > completetime[1]:
                answer += time - completetime[1]
            answer += completetime[0]
            time += completetime[0]
        except:
            if not jobs and not stays:
                return answer // lenjobs
            time += 1