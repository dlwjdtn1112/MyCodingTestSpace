
# 내가 작성한 코드
R,C = map(int,input().split())
cnt = 0
arr = []
for i in range(R):
    arr.append(input())

arr1 = list(zip(*arr))
for lst in arr:
    l1 = lst.split("|")
    for i in l1:
        if i != '':
            cnt += 1

for lst in arr1:
    str = "".join(lst)
    l1 = str.split("-")
    for i in l1:
        if i != '':
            cnt += 1
print(cnt)

#chat gpt
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            # 가로 방향 나무 판자
            if board[i][j] == '-':
                nj = j
                while nj < m and board[i][nj] == '-':
                    visited[i][nj] = True
                    nj += 1
            # 세로 방향 나무 판자
            elif board[i][j] == '|':
                ni = i
                while ni < n and board[ni][j] == '|':
                    visited[ni][j] = True
                    ni += 1

print(count)


















