# chat gpt4o + 이정수

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def bfs(si, sj, ei, ej):
        q = deque()
        q.append((si, sj))
        v = [[0] * m for _ in range(n)]
        v[si][sj] = 1

        while q:
            ci, cj = q.popleft()
            if (ci, cj) == (ei, ej):
                return v[ci][cj]

            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1

        return -1  # 끝까지 못 가면 -1

    return bfs(0, 0, n-1, m-1)

