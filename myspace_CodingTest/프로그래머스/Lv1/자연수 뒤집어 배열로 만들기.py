

# 내가 작성한 코드
def solution(n):
    n_str = str(n)
    n_str_l1 = list(n_str)

    n_str_l1.reverse()
    n_str_l1_r = [int(i) for i in n_str_l1]
    answer = n_str_l1_r

    return answer

print(solution(12345))