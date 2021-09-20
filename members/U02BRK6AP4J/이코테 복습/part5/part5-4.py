'''
BFS(너비 우선 탐색)
- 큐 사용
- 가까운 노드부터 우선 탐색
- 최단 경로 알고리즘에 사용
- DFS와의 다른 점? BFS는 해당 노드의 인접 노드를 한 번에 큐에 넣음 / DFS는 차례대로 인접 노드를 탐색한다는 점에서 차이가 있음
'''
from collections import deque
graph = [
    [],  # 사용하지 않는 0번 노드는 빈 리스트로 처리
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def bfs(graph, idx, visited):
    queue = deque([idx])
    visited[idx] = True
    while queue:
        x = queue.popleft()
        print(x)
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * len(graph)
bfs(graph, 1, visited)
