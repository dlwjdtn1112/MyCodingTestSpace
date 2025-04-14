
# 내가 작성한 코드
def solution(brown, yellow):
    arr = []
    arr1 = []

    # yellow의 약수쌍 구하기
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            arr.append([i, yellow // i])

    # 약수쌍 중에서 세로 ≤ 가로만 선택해서 양쪽 +2 한 후 저장
    for lst in arr:
        if lst[0] >= lst[1]:
            lst[0] += 2
            lst[1] += 2
            arr1.append(lst)

    # 전체 넓이에서 yellow를 뺀 값이 brown이면 정답
    for lst in arr1:
        if lst[0] * lst[1] - yellow == brown:
            return lst
# chat gpt4o
def solution(brown, yellow):
    arr = []
    result = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow // i  # 가로
            h = i            # 세로

            # 테두리 갈색 타일 고려: 가로+2, 세로+2
            total_w = w + 2
            total_h = h + 2

            if total_w * total_h - yellow == brown:
                result = [total_w, total_h]
                break

    return result




