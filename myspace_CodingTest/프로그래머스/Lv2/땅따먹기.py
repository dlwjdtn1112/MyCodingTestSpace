
# 내가 작성한 코드
def solution1(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            result = []
            for k in range(len(land[0])):
                if j == k:
                    pass
                else:
                    result.append(land[i - 1][k])
            land[i][j] = max(result) + land[i][j]

    answer = max(land[len(land) - 1])
    return answer

# chat gpt4o
def solution2(land):
    # DP 방식으로 점화식 계산
    for i in range(1, len(land)):  # 첫 번째 행은 건드리지 않음
        for j in range(4):  # 각 열을 순차적으로
            # 이전 행에서 가로로 인접하지 않는 값 중 가장 큰 값을 더함
            land[i][j] += max(land[i - 1][k] for k in range(4) if k != j)

    # 마지막 행에서 가장 큰 값 반환
    return max(land[-1])


