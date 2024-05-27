"""
1. 모든 경우의 수를 판단해야 하므로 DFS 사용함.
2. 시간복잡도 O(n!) : n개의 경로에서 1개를 선택 후 다음 경로 탐색은 총 n-1 가지임.
                    최악의 경우 n -> n -1 -> n-2 ... 1 까지 진행하여 O(n!)이 된다.
"""

route = []
answer = []
def solution(tickets):
    global answer
    find_route(tickets)
    if len(answer) > 1: # 가능한 모든 경로의 수가 여러가지라면 알파벳 순으로 정리 
        answer = sorted(answer)
    return answer[0]

def find_route(tickets):
    global route
    global answer
    if len(tickets) == 0:  # 모든 깊이까지 다 들어왔다면 정답 list에 경로 추가
        answer.append(make_result(route))
        return
        
    for i in range(len(tickets)):
        ticket = tickets.pop(i)
        if len(route) == 0 and ticket[0] == 'ICN':  # 출발은 항상 ICN에서 출발
            route.append(ticket) 
            find_route(tickets)  # 한층 더 아래로 들어가서 탐색
            route.pop(-1)
        elif len(route) > 0 and route[-1][-1] == ticket[0]: # 이번에 뽑은 경로에서 도착지와 출발지가 같다면 다음 경로 가능
            route.append(ticket)
            find_route(tickets)  # 한층 더 아래로 들어가서 탐색
            route.pop(-1)
        tickets.insert(i, ticket)

def make_result(route):  # 결과는 [출발 도착] 이 아닌 경로 리스트를 리턴
    result= []
    for i in route:
        result.append(i[0])
    result.append(route[-1][-1])
    return result