# 내가 작성한 코드
def solution(n):
    cnt = n // 2
    s1 = "수박"
    if n % 2 == 0:
        answer = s1 * cnt
    else:
        answer = s1 * cnt
        answer += "수"
    return answer