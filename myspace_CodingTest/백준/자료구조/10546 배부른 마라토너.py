
#내가 작성한 코드
from collections import Counter
N  = int(input())

arr = []
arr1 = []
for i in range(N):
    arr.append(input())
for i in range(N-1):
    arr1.append(input())

result = list((Counter(arr) - Counter(arr1)).elements())
print(*result)

# chat gpt
n = int(input())
participants = [input().strip() for _ in range(n)]
completions = [input().strip() for _ in range(n - 1)]

participants.sort()
completions.sort()

for p, c in zip(participants, completions):
    if p != c:
        print(p)
        break
else:
    # 마지막 사람이 완주 못한 경우
    print(participants[-1])





