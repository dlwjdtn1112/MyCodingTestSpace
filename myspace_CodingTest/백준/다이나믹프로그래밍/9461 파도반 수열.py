def dp(n):
    if n <=2:
        return 1
    elif n >=3 and n <=4:
        return 2
    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    dp[3] = 2
    dp[4] = 2

    for i in range(5,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[n]


n = int(input())
l1 = []
for i in range(n):
    a = int(input())
    l1.append(dp(a-1))
for i in l1:
    print(i)