import heapq as h
#heapq.heappush(heap, item) : item을 heap에 추가
#heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴
#heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
"""
1. try except활용하여 heappop 에러시(2개가 없을 경우) K이상 스코빌 달성 불가
2. heappop으로 제일 작은 스코빌음식을 꺼냈을 때 K보다 크다면 정답 반환
3. heappop으로 제일 작은 스코빌 음식을 꺼냈을 때 K보다 작다면 min + sec_min *2 계산 후 heappush
4. 시간복잡도O(nlogn) : 힙 구성 = O(n), 최대 n/2번의(heappop O(logn) + heappush O(logn)) = O(nlogn)
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
