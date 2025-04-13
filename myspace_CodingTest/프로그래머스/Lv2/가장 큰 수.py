# 내가 작성한 코드
from itertools import permutations

def solution(numbers):
    l2 = [str(i) for i in numbers]
    arr = list(permutations(l2, len(numbers)))
    result = [int("".join(i)) for i in arr]
    return max(result)


# chat gpt
from functools import cmp_to_key

def compare(x, y):
    # 두 문자열을 합쳐서 비교
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    l2 = [str(i) for i in numbers]
    # 커스텀 비교 함수로 정렬
    l2.sort(key=cmp_to_key(compare))
    answer = ''.join(l2)
    # '000' 같은 경우는 '0'으로 처리
    return '0' if answer[0] == '0' else answer



