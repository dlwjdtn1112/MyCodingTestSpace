


# 약수를 구하는 알고리즘
def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return len(divisors)


def solution(left, right):
    l1 = []
    l2 = []

    for lst in range(left, right + 1):
        cnt = get_divisors(lst)
        if cnt % 2 == 0:
            l1.append(lst)
        else:
            l2.append(lst)

    answer = sum(l1) - sum(l2)

    return answer



def solution_chatgpt4o(left, right):
    answer = 0
    for i in range(left, right + 1):
        # 제곱수이면 약수 개수는 홀수 → 빼기
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
