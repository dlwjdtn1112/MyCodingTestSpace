def solution(str_list, ex):
    answer = ''
    for lst in str_list:
        if lst.find(ex) != -1:
            pass
        elif lst.find(ex) == -1:
            answer += lst

    return answer