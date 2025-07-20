def solution_ㅡㅛ(s1, s2):
    answer = 0

    for lst in s1:
        for i in s2:
            if lst == i:
                answer += 1
    return answer