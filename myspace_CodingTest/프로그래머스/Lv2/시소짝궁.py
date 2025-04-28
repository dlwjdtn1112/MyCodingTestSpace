def solution1(weight): # 내가 작성한 코드(시간초과)
    result = 0

    for i in range(len(weight)):
        for j in range(i + 1, len(weight)):
            if weight[i] == weight[j]:
                result += 1
            else:
                for lst in [[3, 2], [4, 3], [4, 2]]:
                    if weight[i] < weight[j]:
                        if weight[i] * lst[0] == weight[j] * lst[1]:
                            result += 1

                    else:
                        if weight[i] * lst[1] == weight[j] * lst[0]:
                            result += 1

    return result


#chat gpt4o
from collections import Counter


def solution2(weight):
    answer = 0
    counter = Counter(weight)
    weights = sorted(counter.keys())  # 정렬된 고유 weight 리스트

    for w in weights:
        cnt = counter[w]
        # 자기 자신 짝꿍 (같은 무게 2명 이상이면 조합 nC2)
        if cnt >= 2:
            answer += cnt * (cnt - 1) // 2

        # 2:3, 2:4, 3:4 비율 짝꿍 찾기
        for a, b in [(2, 3), (2, 4), (3, 4)]:
            target = w * b / a
            if target == int(target) and target in counter:
                answer += cnt * counter[int(target)]

    return answer

