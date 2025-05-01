
# 내가 작성한 코드(시간 초과 정확도 79.2%)
def solution1(k, m, score):
    result = 0
    v1 = len(score) // m
    score_s = sorted(score, reverse=True)
    cnt = 0
    for i in range(v1):
        arr = []
        for i in range(m):
            arr.append(score_s.pop(0))
        min1 = min(arr)
        cnt += min1 * len(arr)
    return cnt

#chat gpt4o

def solution2(k, m, score):
    result = 0
    v1 = len(score) // m
    score_s = sorted(score, reverse=True)
    cnt = 0

    for i in range(v1):
        arr = score_s[i * m : (i + 1) * m]  # 슬라이싱으로 사과 m개 묶음
        min1 = min(arr)
        cnt += min1 * len(arr)

    return cnt
