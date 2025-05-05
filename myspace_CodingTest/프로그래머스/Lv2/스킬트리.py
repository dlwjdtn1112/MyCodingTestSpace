
# 내가 작성한 코드
def solution1(skill, skill_trees):
    s_list = list(skill)
    result = 0

    for lst in skill_trees:
        s1 = ""
        for i in lst:
            if i in s_list:
                s1 += i
        if skill.startswith(s1) == True:
            result += 1

    return result

# chat gpt4o
def solution2(skill, skill_trees):
    result = 0
    for tree in skill_trees:
        filtered = [s for s in tree if s in skill]
        if skill.startswith(''.join(filtered)):
            result += 1
    return result

def solution3(skill, skill_trees):
    from collections import deque

    result = 0
    for tree in skill_trees:
        q = deque(skill)
        for s in tree:
            if s in skill:
                if s != q[0]:
                    break
                q.popleft()
        else:
            result += 1
    return result

