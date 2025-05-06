# 내가 작성한 코드
from collections import deque

def solution1(priorities, location):
    cnt = 0
    priorities_sorted = sorted(priorities, reverse=True)
    alpha = [chr(65+i) for i in range(len(priorities))]

    priorities_dict = dict(zip(alpha, priorities))
    priorities_dict_deque = deque(priorities_dict)

    location_alpha = alpha[location]
    result = 0

    while True:
        if priorities_dict[priorities_dict_deque[0]] == priorities_sorted[cnt]:
            if priorities_dict_deque[0] == location_alpha:
                result += 1
                priorities_dict_deque.popleft()
                break
            else:
                priorities_dict_deque.popleft()
                result += 1
                cnt += 1
        else:
            priorities_dict_deque.rotate(-1)

    return result

# chat gpt4o
from collections import deque

def solution2(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        cur = queue.popleft()
        if any(cur[0] < other[0] for other in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[1] == location:
                return order
