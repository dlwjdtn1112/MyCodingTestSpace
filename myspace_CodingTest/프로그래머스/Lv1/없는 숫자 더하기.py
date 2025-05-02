
# 내가 작성한 코드
def solution1(numbers):
    answer = 0
    check_arr = [i for i in range(10)]

    for lst in check_arr:
        if lst not in numbers:
            answer += lst

    return answer

#chat gpt4o
def solution2(numbers):
    return 45 - sum(numbers)

