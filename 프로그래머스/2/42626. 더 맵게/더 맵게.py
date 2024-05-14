import heapq as h
#heapq.heappush(heap, item) : item을 heap에 추가
#heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴
#heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )

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