# 내가 작성한 코드
from itertools import permutations


def solution1(number, k):
    s1 = list(number)
    arr = [i for i in range(len(s1))]

    # 남겨야 할 인덱스 수
    keep_len = len(s1) - k

    # 인덱스를 뽑는 조합 (중복 제거 위해 set 사용)
    arr1 = set(permutations(arr, keep_len))

    result = []

    for i in arr1:
        i = list(i)
        i.sort()  # 순서 유지
        result.append(i)

    result1 = []

    for lst in result:
        s2 = ''
        for i in lst:
            s2 += s1[i]
        result1.append(s2)

    m1 = max(result1)
    return m1
# chat gpt4o
from itertools import combinations

def solution(number, k):
    s1 = list(number)
    arr = [i for i in range(len(s1))]

    keep_len = len(s1) - k

    # 조합으로 필요한 인덱스 선택 (순서 유지 보장)
    arr1 = combinations(arr, keep_len)

    max_val = "0"

    for idx_list in arr1:
        s = ''.join(s1[i] for i in idx_list)
        if s > max_val:
            max_val = s

    return max_val
