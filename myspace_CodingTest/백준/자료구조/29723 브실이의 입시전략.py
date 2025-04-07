
a,b,c = map(int,input().split())
arr = []
arr1 = []
for i in range(a):
    l1  = list(input().split())
    l1[1] = int(l1[1])
    arr.append(l1)
cnt = 0

for i in range(c):
    arr1.append(input())
for i in arr1:
    for j in arr:
        if i == j[0]:
            cnt += j[1]
            arr.remove(j)


arr_s = sorted(arr,key=lambda x:x[1])



max1 = cnt
min1 = cnt

for i in range(b-c):
    min1 += arr_s[i][1]
arr_s.reverse()

for i in range(b-c):
    max1  += arr_s[i][1]
print(min1,max1)
