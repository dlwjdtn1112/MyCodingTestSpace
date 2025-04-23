def solution(maps):
    def bfs(si, sj):
        q = []
        cnt = 0
        q.append((si, sj))
        cnt += arr[si][sj]
        v[si][sj] = 1
        while q:
            ci, cj = q.pop(0)
            for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < l1 and 0 <= nj < l2 and v[ni][nj] == 0 and arr[ni][nj] != 0:
                    v[ni][nj] = 1
                    cnt += arr[ni][nj]
                    q.append((ni, nj))
        return cnt

    l1 = len(maps)
    l2 = len(maps[0])
    v = [[0]*l2 for _ in range(l1)]
    arr = []
    for lst in maps:
        arr.append(list(lst))

    for i in range(l1):
        for j in range(l2):
            if arr[i][j] == 'X':
                arr[i][j] = 0
            else:
                arr[i][j] = int(arr[i][j])

    result = []
    for i in range(l1):
        for j in range(l2):
            if arr[i][j] != 0 and v[i][j] == 0:
                result.append(bfs(i, j))

    result.sort()
    if len(result) == 0:
        return [-1]
    else:
        return result
