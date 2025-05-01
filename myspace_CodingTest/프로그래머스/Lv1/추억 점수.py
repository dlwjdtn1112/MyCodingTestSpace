#내가 작성한 코드

def solution1(name, yearning, photo):
    result = []

    new_arr  = dict(zip(name, yearning))

    for lst in photo:
        cnt = 0
        for i in lst:
            if i in new_arr:
                cnt += new_arr[i]
        result.append(cnt)

    return result

#chat gpt4o
def solution2(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    return [sum(score_map.get(person, 0) for person in group) for group in photo]

