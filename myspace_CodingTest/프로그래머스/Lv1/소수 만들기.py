from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))

    for lst in arr:
        a = sum(lst)
        if is_prime(a) == True:
            answer += 1

    return answer

