def solution_my(array, height):
    answer = 0

    for i in array:
        if height < i:
            answer += 1

    return answer