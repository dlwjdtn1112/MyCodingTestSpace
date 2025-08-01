# 그래프 정의 (이미지에서 제공된 데이터)
graph = {
    0: [1, 3, 6],
    1: [2, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

# 방문 여부를 저장할 딕셔너리
# 모든 노드를 False로 초기화
visited = {node: False for node in graph}


# DFS 함수 정의
def dfs(cur_v):
    # 현재 노드를 방문했음을 표시
    visited[cur_v] = True

    print(cur_v, end=' ')  # 탐색 순서 출력 (선택 사항)

    # 현재 노드와 연결된 모든 이웃 노드들을 순회
    for next_v in graph[cur_v]:
        # 만약 이웃 노드가 아직 방문되지 않았다면
        if not visited[next_v]:
            # 재귀적으로 DFS를 호출하여 탐색을 이어감
            dfs(next_v)


# DFS 시작 (예: 노드 0에서 시작)
print("DFS 탐색 순서:")
dfs(0)