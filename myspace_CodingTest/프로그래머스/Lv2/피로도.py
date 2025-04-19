
# 내가 작성한 코드
from itertools import permutations


def solution1(k, dungeons):
    l1 = [i for i in range(len(dungeons))]

    result = []
    arr = list(permutations(l1, len(l1)))

    for lst in arr:
        temp_k = k  # k를 원본에서 유지하기 위해 temp 변수 사용
        cnt = 0
        for i in lst:
            if temp_k >= dungeons[i][0]:
                temp_k -= dungeons[i][1]
                cnt += 1
        result.append(cnt)

    return max(result)



#chat gpt4o
from itertools import permutations

def solution2(k, dungeons):
    max_cnt = 0
    for order in permutations(range(len(dungeons)), len(dungeons)):
        temp_k = k
        cnt = 0
        for i in order:
            min_req, cost = dungeons[i]
            if temp_k >= min_req:
                temp_k -= cost
                cnt += 1
        max_cnt = max(cnt, max_cnt)

    return max_cnt


def solution3(k, dungeons):
    n = len(dungeons)
    max_cnt = 0
    visited = [False] * n

    def dfs(current_k, depth):
        nonlocal max_cnt

        max_cnt = max(max_cnt, depth)

        for i in range(n):
            if not visited[i]:
                min_req, cost = dungeons[i]
                if current_k >= min_req:
                    visited[i] = True
                    dfs(current_k - cost, depth + 1)
                    visited[i] = False

    dfs(k, 0)
    return max_cnt
