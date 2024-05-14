"""
1 .heapq는 첫 번째 요소를 기준으로 힙 구성
2. 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리
3. 작업이 끝났을 때 요청들어온 작업들이 여러 개라면, 작업 시간이 작은 작업부터 처리
4. 시간복잡도O(nlogn) : 힙 구성 = O(n), 최대 n번의(heappop O(logn) + heappush O(logn)) = O(nlogn)
5. 헤맨 부분 : 문제의 소수점 나머지는 버리는 부분 놓쳐서 계속 틀림
6. 아쉬운 점 : 맨 마지막 time += 1 -> 여기서 불필요한 반복문이 계속됨 -> 작업 대기중인heap의 가장 작은 요청시간을 time에 더해버리면 불필요한 반복문 줄어들 것으로 예상
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
