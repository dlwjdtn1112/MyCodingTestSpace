


# 내가 작성한 코드
result = []
n = int(input())

for _ in range(n):
    cnt = 0
    a,b  = map(int,input().split())
    l1 = list(map(int,input().split()[:a]))
    l2 = list(map(int, input().split()[:b]))
    l1.sort()
    l2.sort()
    if len(l1) == len(l2):
        if l1 == l2:
            result.append("=")
        else:
            result.append("?")
    elif len(l1) > len(l2):
        for i in l2:
            if i in l1:
                cnt += 1
        if cnt == len(l2):
            result.append(">")
        else:
            result.append("?")

    elif len(l1) < len(l2):
        for i in l1:
            if i in l2:
                cnt += 1
        if cnt == len(l1):
            result.append("<")
        else:
            result.append("?")

for lst in result:
    print(lst)

# chat gpt4o
T = int(input())
for _ in range(T):
    len_a, len_b = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    if A == B:
        print("=")
    elif A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("?")

