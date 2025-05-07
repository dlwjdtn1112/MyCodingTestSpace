#내가 작성한 코드
from collections import deque
import math

def solution1(progresses, speeds):
    result = []
    days_queue = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])

    while days_queue:
        current = days_queue.popleft()
        count = 1

        while days_queue and days_queue[0] <= current:
            days_queue.popleft()
            count += 1

        result.append(count)

    return result

# chat gpt4o
from collections import deque
import math

def solution2(progresses, speeds):
    result = []
    days_queue = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])

    while days_queue:
        current = days_queue.popleft()
        count = 1

        while days_queue and days_queue[0] <= current:
            days_queue.popleft()
            count += 1

        result.append(count)

    return result

