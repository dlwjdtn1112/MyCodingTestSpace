# from itertools import combinations
#
# result = []
#
#
#
#
# T = int(input())
#
# for _ in range(T):
#     arr = [[] for _ in range(30)]
#     l1 = []
#     l2 = []
#     l4 = []
#     a,b = map(int,input().split())
#     for i in range(b):
#         c,d = map(int,input().split())
#         arr[c].append(d)
#         l1.append(c)
#
#     for j in range(1,b+1):
#         l3 = list(combinations(l1,j))
#         for lst in l3:
#             if sum(lst) <= a:
#                 if list(set(lst))  not in l2:
#                     l2.append(list(set(lst)))
#
#
#
#
#
#
#
#     for lst in l2:
#         cnt = 0
#         for lst1 in lst:
#             cnt += sum(arr[lst1])
#
#         l4.append(cnt)
#
#     result.append(max(l4))
#
# for i in range(len(result)):
#     print("#"+str(i+1) , result[i])

def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())  # N: 박스 용량, M: 물건 수
        items = [tuple(map(int, input().split())) for _ in range(M)]  # (size, price)

        memo = {}  # (i, cap) -> 최대 가격

        def dfs(i, cap):
            key = (i, cap)
            if key in memo:
                return memo[key]
            if i == M:
                return 0

            # 1) i번째 물건을 선택하지 않는 경우
            best = dfs(i + 1, cap)

            # 2) i번째 물건을 선택하는 경우 (용량 가능 시)
            s, p = items[i]
            if s <= cap:
                cand = p + dfs(i + 1, cap - s)
                if cand > best:
                    best = cand

            memo[key] = best
            return best

        ans = dfs(0, N)
        print(f"#{tc} {ans}")

if __name__ == "__main__":
    solve()







