
# 내가 작성한 코드
def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    boats = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가장 가벼운 사람 태움
        j -= 1  # 가장 무거운 사람 태움 (항상 보트에 한명은 무조건 타야 하니까)
        boats += 1

    return boats






