
N = int(input())

dp = [0] * (N + 1)

arr = [0] + list(map(int,input().split()))

for i in range(1,N+1):
    mx = 0
    for j in range(0,i):
        if arr[i] > arr[j]:
            mx = max(mx,dp[j])
        dp[i] = mx + 1

print(max(dp))

