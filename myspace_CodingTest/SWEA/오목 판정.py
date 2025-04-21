


def solve():
    for si in range(N):
        for sj in range(N):
            for di,dj in [[0,1],[1,0],[1,1],[-1,1]]:
                for mul in range(5):
                    ni,nj = si + (di * mul),sj + (dj * mul)
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        pass
                    else:
                        break
                else:
                    return "YES"
    else:
        return "No"

N = int(input())

for test_case in range(1,N+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = solve()
    print(f'#{test_case} {ans}')














