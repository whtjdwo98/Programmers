# [배경 지식]
![인접행렬](https://github.com/whtjdwo98/Programmers/assets/37203984/241cd6d4-2a0b-4474-a102-af347714af47)
1. 인접 행렬 : 노드(V)와 간선(E)을 2차원 배열 형태로 나타낸 구조
2. 장점 : 구현이 쉬움, 간선 존재 확인을 빠르게 가능
3. 단점 : 간선이 많지 않다면 공간 낭비 발생
![인접리스트](https://github.com/whtjdwo98/Programmers/assets/37203984/7df42e7e-02c0-44a0-afaf-4c107df74cf3)
4. 인접 리스트 : 노드(V)와 간선(E)을 링크드 리스트 형태로 나타낸 구조
5. 장점 : 꼭 필요한 메모리 공간만 사용 가능
6. 단점 : 두 노드간에 간선 존재 확인을 위해 연결리스트를 모두 확인해야 하기 때문에 최악의 경우 O(V)의 시간복잡도를 가짐

![DFS](https://github.com/whtjdwo98/Programmers/assets/37203984/1065ec9b-ca67-406a-92eb-56c4db62c942)
1. DFS(깊이 우선 탐색)
2. 구현 시 사용되는 자료구조 : Stack, 재귀함수
3. 주로 사용되는 문제 : 모든 정점 탐색, 가중치가 있는 정점 탐색
4. 시간복잡도 : 인접 리스트 시간 복잡도: O(V + E), 인접 행렬 시간 복잡도: O(V^2)
5. 간단한 DFS 탐색 코드 구조
```Python
def DFS():
  if 탈출 조건:
    return
  반복문(현재 정점에서 탐색할 수 있는 모든 정점):
    if 탐색 조건:
     DFS()
```

![BFS](https://github.com/whtjdwo98/Programmers/assets/37203984/574dec12-cc10-46db-ae04-a893f51650ac)
1. BFS(넓이 우선 탐색)
2. 구현 시 사용되는 자료구조 : Quque
3. 주로 사용되는 문제 : 모든 정점 탐색, 최단거리 탐색
4. 시간복잡도 : 인접 리스트 시간 복잡도: O(V + E), 인접 행렬 시간 복잡도: O(V^2)
5. 간단한 BFS 탐색코드 구조
```Python
def BFS():
  queue.append(루트노드)
  반복문(queue가 비었을 때까지):
    현재 노드 = queue.pop()
    현재 노드에서 할 작업 진행
    현재 노드에서 조건에 만족하는 모든 정점 queue.append

```
