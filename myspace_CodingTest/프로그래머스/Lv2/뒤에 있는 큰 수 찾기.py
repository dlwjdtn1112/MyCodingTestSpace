# 내가 작성한 코드
def solution(numbers):
    result = []
    for i in range(len(numbers)):
        de = -1
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                de = numbers[j]
                break
        result.append(de)
    return result



#chat gpt4o
def solution(numbers):
    result = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        # 스택에 있는 인덱스의 값보다 현재 값이 크면,
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            result[idx] = numbers[i]
        stack.append(i)

    return result