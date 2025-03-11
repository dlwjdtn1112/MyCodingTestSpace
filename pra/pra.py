a,b = map(int,input().split())

l1 = list(map(int,input().split()[:a]))

count = 0

sum = 0
end = 0

for i in range(len(l1)):
    while sum < b and end < len(l1):
        sum += l1[end]
        end += 1

    if sum == b:
        count +=1
    sum -= l1[i]

print(count)



