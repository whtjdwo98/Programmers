import heapq as h
#heapq.heappush(heap, item) : item을 heap에 추가
#heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴
#heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""
1. try except활용하여 heappop 에러시(2개가 없을 경우) K이상 스코빌 달성 불가
2. heappop으로 제일 작은 스코빌음식을 꺼냈을 때 K보다 크다면 정답 반환
3. heappop으로 제일 작은 스코빌 음식을 꺼냈을 때 K보다 작다면 min + sec_min *2 계산 후 heappush
4. 시간복잡도O(nlogn) : 힙 구성 = O(n), 최대 n/2번의(heappop O(logn) + heappush O(logn)) = O(nlogn)
5. scoville의 길이 정보를 len(scoville)로 확인하는게 더 느리다고 생각하여 try except로 예외처리를 하였지만,
   len(scoville)함수가 O(1)로 훨씬 더 빠르다는 것을 알게 되었음. try except는 예외처리 오버헤드가 존재하여 더 느림.
"""

def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while 1:
        try:
            min = h.heappop(scoville)
            if min >= K:
                return answer
            sec_min = h.heappop(scoville)
            h.heappush(scoville, min + (sec_min * 2))
            answer += 1
        except:
            return -1
    return answer
