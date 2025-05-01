# 내가 작성한 코드

def solution1(answer):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]

    for i in range(len(answer)):
        if one[i % len(one)] == answer[i]:
            result[0] += 1
        if two[i % len(two)] == answer[i]:
            result[1] += 1
        if three[i % len(three)] == answer[i]:
            result[2] += 1

    m1 = max(result)
    result2 = []
    for i in range(len(result)):
        if result[i] == m1:
            result2.append(i + 1)
    return result2


# chat gpt4o
def solution2(answer):
    patterns = [
        [1, 2, 3, 4, 5],                # 수포자 1
        [2, 1, 2, 3, 2, 4, 2, 5],       # 수포자 2
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 3
    ]

    scores = [
        sum(1 for i, a in enumerate(answer) if a == pattern[i % len(pattern)])
        for pattern in patterns
    ]

    max_score = max(scores)

    return [i + 1 for i, score in enumerate(scores) if score == max_score]
