

#내가 작성한 코드
def solution(want, number, discount):
    arr = dict(zip(want, number))
    cnt = 0
    for i in range(len(discount) - 9):
        result = []
        cnt_l1 = []
        for j in range(i, i + 10):
            result.append(discount[j])
        for k in want:
            cnt_l1.append(result.count(k))
        if cnt_l1 == number:
            cnt += 1

    if cnt == 0:
        return 0
    else:
        return cnt




#chat gpt4o
from collections import Counter

def solution(want, number, discount):
    target = dict(zip(want, number))
    answer = 0

    for i in range(len(discount) - 9):
        window = discount[i:i+10]
        count = Counter(window)

        if all(count.get(item, 0) >= target[item] for item in target):
            answer += 1

    return answer

