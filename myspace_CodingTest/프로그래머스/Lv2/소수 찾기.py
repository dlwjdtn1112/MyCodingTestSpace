# 내가 작성한 코드
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution1(numbers):
    a = list(numbers)
    result = []
    result2 = []

    for i in range(1, len(a)+1):
        arr = list(permutations(a, i))
        for lst in arr:
            result.append(lst)

    cnt = 0
    for i in result:
        result_i = list(i)
        result_str = "".join(result_i)
        result2.append(result_str)

    result_set = set(result2)
    result_set1 = set([int(i) for i in result_set])

    for i in result_set1:
        if is_prime(i):
            cnt += 1

    return cnt

#chat gpt4o
from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution2(numbers):
    candidate_set = set()

    # 가능한 모든 순열 조합을 문자열 → 정수로 변환
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            candidate_set.add(num)

    # 소수 판별 후 카운트
    return sum(1 for x in candidate_set if is_prime(x))


