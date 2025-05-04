# 내가 작성한 코드
def solution(board, h, w):
    result = 0
    v1 = board[h][w]

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = h + di, w + dj
        if 0 <= ni < len(board[0]) and 0 <= nj < len(board[0]):
            if board[ni][nj] == v1:

                result += 1
            else:
                pass

    return result