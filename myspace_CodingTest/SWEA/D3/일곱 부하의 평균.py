
result = []
T = int(input())

for _ in range(T):
    arr = list(map(int,input().split()[:6]))
    s1 = max(arr)
    while True:
        if ((sum(arr) + s1) / (len(arr) + 1)).is_integer():
            result.append(s1)
            break
        else:
            s1 += 1

for i in range(len(result)):
    print(result[i])


# l1 = [100,100,200,200,300,300,306]
# print((sum(l1)/len(l1)).is_integer())