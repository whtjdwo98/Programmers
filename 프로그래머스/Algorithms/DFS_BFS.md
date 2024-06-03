![DFS](https://github.com/whtjdwo98/Programmers/assets/37203984/1065ec9b-ca67-406a-92eb-56c4db62c942)
1. DFS(깊이 우선 탐색)
2. 구현 시 사용되는 자료구조 : Stack, 재귀함수
3. 주로 사용되는 문제 : 모든 정점 탐색, 가중치가 있는 정점 탐색
4. 간단한 DFS 탐색 코드 구조
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
4. 간단한 BFS 탐색코드 구조
```Python
def BFS():
  queue.append(루트노드)
```
