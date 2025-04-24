

# 내가 작성한 코드
def solution(s1):
    stack = []
    stack.append(s1[0])

    for i in range(1, len(s1)):
        if s1[i] == "(":
            stack.append(s1[i])
        elif s1[i] == ")":
            if stack and stack[len(stack)-1] == "(":
                stack.pop(-1)
        # print(stack)  ← 제출용에선 주석 처리 (테스트 디버깅용이면 유지 가능)

    if len(stack) == 0:
        return True
    else:
        return False


# ChatGPT 4o
def solution(s):
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:  # ch == ")"
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False  # 짝이 안 맞는 경우 즉시 실패

    return len(stack) == 0
