'''
그래프
- 노드(=정점, v)와 간선(e)으로 이루어짐
- 인접 행렬(빠름) 혹은 인접 리스트 형태(메모리 효율적)로 나타낼 수 있음
- 인접 행렬: 각 노드의 인접 노드 정보를 행렬로 나타냄(0: 자기 자신, INF: 접하지 않음)
- 인접 리스트: 각 노드들이 갖는 인접한 노드 리스트를 값으로 가짐
DFS(깊이 우선 탐색)
- 스택 혹은 재귀함수 사용
- 작은 노드부터 우선 탐색
'''
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

def dfs(graph, idx, visited):
    visited[idx] = True
    print(idx)
    for i in graph[idx]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * len(graph)
dfs(graph, 1, visited)
