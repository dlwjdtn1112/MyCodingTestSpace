def solution_my(s, n):
    s_list = list(s)
    result = []
    for i in s_list:
        if i == ' ':
            result.append(' ')
        else:
            if 65 <= ord(i) <= 90:
                cnt = n + ord(i)
                if cnt > 90:
                    cnt1 = cnt - 90 - 1
                    result.append(chr(cnt1 + 65))
                else:
                    result.append(chr(cnt))
            else:
                cnt = n + ord(i)
                if cnt > 122:
                    cnt1 = cnt - 122 - 1
                    result.append(chr(cnt1 + 97))
                else:
                    result.append(chr(cnt))
    return "".join(result)


def solution_chatGpt4o(s, n):
    s_list = list(s)
    result = []
    for i in s_list:
        if i == ' ':
            result.append(' ')
        else:
            if 65 <= ord(i) <= 90:
                cnt = n + ord(i)
                if cnt > 90:
                    cnt1 = cnt - 90 - 1
                    result.append(chr(cnt1 + 65))
                else:
                    result.append(chr(cnt))
            else:
                cnt = n + ord(i)
                if cnt > 122:
                    cnt1 = cnt - 122 - 1
                    result.append(chr(cnt1 + 97))
                else:
                    result.append(chr(cnt))
    return "".join(result)
