

#내가 작성한 코드
def solution(d, budget):
    len_d = len(d)
    d.sort()
    v1 = 0
    for i in range(len_d, 0, -1):
        if sum(d[0:i]) > budget:
            continue
        else:
            v1 = i
            break
    return v1


#chat gpt4o
def solution1(d, budget):
    d.sort()
    count = 0
    for cost in d:
        if budget >= cost:
            budget -= cost
            count += 1
        else:
            break
    return count


