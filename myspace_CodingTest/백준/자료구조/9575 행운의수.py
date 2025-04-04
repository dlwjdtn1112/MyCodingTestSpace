# 내가 작성한 코드
s1 = {'5'}
s2 = {'8'}
s3 = {'5','8'}

N = int(input())

result = []

for _ in range(N):
    num = 0
    l1 = []
    a = int(input())
    arr1 = list(map(int,input().split()[:a]))
    b = int(input())
    arr2 = list(map(int,input().split()[:b]))
    c  = int(input())
    arr3 = list(map(int,input().split()[:c]))
    for i in arr1:
        for j in arr2:
            for k in arr3:
                l1.append(i+j+k)

    s4 = set(l1)

    for lst in s4:
        if set(str(lst)) == s1 or set(str(lst)) == s2 or set(str(lst)) == s3:
            num += 1
    result.append(num)
for i in result:
    print(i)

# chatGpt4o가 작성한 코드

def is_lucky(n):
    return set(str(n)) <= {'5', '8'}

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    C = list(map(int, input().split()))

    lucky_set = set()
    for a in A:
        for b in B:
            for c in C:
                total = a + b + c
                if is_lucky(total):
                    lucky_set.add(total)
    print(len(lucky_set))




