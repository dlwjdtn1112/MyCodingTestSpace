def solution(s):
    answer = ''
    l1 = []
    l2 = []
    for i in s:
        if i.isupper():
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l1.reverse()
    l2.sort()
    l2.reverse()
    answer += "".join(l2)
    answer += "".join(l1)
    return answer