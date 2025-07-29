result = []

n = int(input())

l1 = [1,2,3,4,5,6]
l2 = ['red','orange','yellow','green','blue','purple']
l3 = dict(list(zip(l2,l1)))

for _ in range(n):
    a,b = input().split()

    if abs(l3[a]  - l3[b]) == 1 or (a == 'red' and b == 'purple') or (b == 'red' and a == 'purple'):
        result.append('A')
    elif abs(l3[a]  - l3[b]) == 3:
        result.append('C')
    elif a == b:
        result.append('E')
    else:
        result.append('X')

for i in range(len(result)):
    print(result[i])