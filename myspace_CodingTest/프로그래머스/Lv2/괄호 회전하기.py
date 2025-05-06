# 내가 작성한 코드
from collections import deque

def solution(s):
    result = 0
    s_deque = deque(s)
    pair = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):
        result1 = "True"
        stack = []
        for char in s_deque:
            if char in '({[':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack[-1] != pair[char]:
                    result1 = "False"
                    break
                stack.pop()
        if result1 == "True" and len(stack) == 0:
            result += 1
        s_deque.rotate(-1)
    return result