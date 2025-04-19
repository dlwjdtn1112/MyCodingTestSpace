# 내가 작성한 코드

def solution(s):
    stack = []

    s1 = list(s)

    result = 0

    stack.append(s1[0])

    l2 = []
    s1.pop(0)

    for i in s1:
        if len(stack) == 0 or i != stack[len(stack) - 1]:
            stack.append(i)
        elif i == stack[len(stack) - 1]:
            stack.pop(-1)

    if len(stack) == 0:
        return 1
    else:
        return 0

# chat gpt4o
from collections import deque

def solution(s):
    s = deque(s)
    stack = []

    while s:
        c = s.popleft()
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return 1 if not stack else 0
