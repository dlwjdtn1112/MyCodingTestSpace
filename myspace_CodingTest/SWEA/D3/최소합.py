
result = []
n1 = int(input())

for _ in range(n1):
    arr = []
    a = int(input())
    dp = [[0] * (a + 1) for _ in range(a+1)]
    arr.append([0] * (a + 1))
    for _ in range(a):
        arr.append([0] + list(map(int,input().split())))
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            if i != 1 and j != 1:
                dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    result.append(dp[a][a])

for i in range(len(result)):
    print("#"+str(i+1) , result[i])































