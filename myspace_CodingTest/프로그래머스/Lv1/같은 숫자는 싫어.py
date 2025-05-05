#내가 작성한 코드
def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer