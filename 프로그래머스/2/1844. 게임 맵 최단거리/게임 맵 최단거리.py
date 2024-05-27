"""
1. Queue 사용하여 BFS 구현함
2. 시간복잡도 O(n^2) : map의 각 위치에서 4방향 유효성 및 거리 계산 O(n^2)
3. 아쉬운 점 : 처음에 DFS를 사용하여 코딩하였으나 효율성에서 시간초과 발생 -> BFS로 변경하여 진행
"""
def solution(maps):
    init(maps)
    return find_load(maps, [0, 0], 1)

def init(maps):
    global direction
    global destination
    maps[-1][-1] = -1 # 목적지 좌표는 -1로 초기화
    destination = [len(maps) -1, len(maps[0]) -1] # 목적지 좌표
    direction = [[1,0], [0,1], [-1,0], [0,-1]]   # 4방향 리스트
    
def find_load(maps, cur_loc, distance):
    queue = []  # BFS를 위해 Queue 선언
    queue.append([cur_loc, distance]) # Queue에는 현재 좌표와 초기 좌표로 부터 이동한 거리를 삽입
    while(len(queue) > 0):
        bfs = queue.pop(0) # Queue에서 현재 좌표를 뺀 후 
        current = bfs[0] # 현재 좌표는 current에 대입
        for dir in direction: # 현재 좌표에서 이동할 수 있는 4방향 모두 검사
            next_loc = [current[0] + dir[0], current[1] + dir[1]] # 다음 좌표를 next_loc으로 초기화 한 후
            if loc_validate(maps, next_loc, bfs[1] + 1): # next_loc이 유효한 좌표값인지 판단 후
                queue.append([next_loc, bfs[1]+1]) #유효한 좌표 값이라면 Queue에 추가한다.
                maps[next_loc[0]][next_loc[1]] = bfs[1]+1 #해당 좌표까지 이동한 거리를 map에 업데이트 한다.
    return maps[-1][-1] # queue의 값이 모두 검사되었다면, 해당 좌표의 거리 값을 리턴

def loc_validate(maps, next_loc, distance):
    # 아래 유효성 검사는 좌표가 map을 초과 여부
    # 다음 좌표의 이동 거리가 현재 계산한 이동거리 보다 짧은지 여부를 판단함.
    if 0 > next_loc[0] or next_loc[0] > destination[0]:
        return False
    if 0 > next_loc[1] or next_loc[1] > destination[1]:
        return False
    if maps[next_loc[0]][next_loc[1]] == 0:
        return False
    if maps[next_loc[0]][next_loc[1]] == -1 or maps[next_loc[0]][next_loc[1]] == 1:
        return True
    if maps[next_loc[0]][next_loc[1]] <= distance:
        return False
    return True