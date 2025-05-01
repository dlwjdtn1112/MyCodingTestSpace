# 내가 작성한 코드

def solution1(cards1, cards2, goal):
    result = "Yes"
    for i in range(len(goal)):
        if len(cards1) > 0 and goal[i] == cards1[0]:
            cards1.remove(cards1[0])
        elif len(cards2) > 0 and goal[i] == cards2[0]:
            cards2.remove(cards2[0])
        else:
            result = "No"
            break
    return result
# chat gpt4o
def solution2(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
