
# 내가 작성한 코드
def solution(strings, n):
    answer = []
    answer = sorted(strings,key = lambda x:(x[n],x))
    return answer