# 내가 작성한 코드

def solution(board):
    row = len(board)
    col = len(board[0])

    dt = [[0 for _ in range(col + 1)]]
    dp = [[0 for _ in range(col + 1)]]

    for i in range(row):
        dt.append([0] + board[i])
        dp.append([0 for _ in range(col + 1)])

    mx = 0
    for i in range(row + 1):
        for j in range(col + 1):
            if dt[i][j]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                mx = max(mx, dp[i][j])

    return mx ** 2
