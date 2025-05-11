n = int(input())
l1=['a','e','i','o','u']
l2=[]
for i in range(n):
    a = input()
    s1 = ""
    for i in a:
        if i not in l1:
            s1 += i
    l2.append(s1)

for i in range(n):
    print("#"+str(i+1), l2[i])