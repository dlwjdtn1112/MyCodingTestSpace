def solution(s):
    result = ""
    cnt = 0
    arr = list(s)
    for i in arr:
        if cnt % 2 == 0 and i != ' ':
            result += i.upper()
            cnt += 1
        elif cnt % 2 != 0 and i != ' ':
            result += i.lower()
            cnt += 1
        elif i == ' ':
            cnt = 0
            result += ' '

    return result




