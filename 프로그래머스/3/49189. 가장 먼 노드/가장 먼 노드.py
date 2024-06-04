distance_list = []
graph = {}
def solution(n, edge):
    init(n, edge)
    return find_distance()

def init(n, edge):
    global distance_list
    global graph
    distance_list = [1] * (n + 1)  #거리 리스트 노드 수 만큼 초기화
    distance_list[0] = 1
    for i in edge:  #주어진 edge를 python dictionary로 선언
        if i[0] in graph:  #양방향 간선이기 때문에 조건문 2개 사용하여 dictionary에 정보 삽입
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]
        if i[1] in graph:
            graph[i[1]].append(i[0])
        else:
            graph[i[1]] = [i[0]]

def find_distance():
    global distance_list
    global graph
    queue = [1]
    distance = 1
    while len(queue) > 0: #노드1 에서 각노드까지의 최단 거리 계산
        current = queue.pop(0)
        
        temp = graph[current]
        distance = distance_list[current] + 1
        for i in temp:
            if (distance_list[i] == 1 or distance_list[i] > distance) and i != 1:
                queue.append(i)
                distance_list[i] = distance
    maximum = max(distance_list) #최댄거리 계산 후 최대값의 갯수 리턴
    return distance_list.count(maximum)