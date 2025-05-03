
# 내가 작성한 코드
def solution2(elements):
    l1 = elements + elements
    arr = []
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            arr.append(sum(l1[j:i + j]))
    return len(set(arr))

#chat gpt 4o
def solution3(elements):
    n = len(elements)
    elements = elements * 2  # 원형 처리
    prefix = [0] * (2 * n + 1)

    # 누적합 배열 생성
    for i in range(1, 2 * n + 1):
        prefix[i] = prefix[i-1] + elements[i-1]

    result = set()
    for length in range(1, n + 1):         # 부분 수열 길이
        for start in range(n):             # 시작 인덱스 (0~n-1까지만 보면 됨)
            end = start + length
            total = prefix[end] - prefix[start]
            result.add(total)

    return len(result)
