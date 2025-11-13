
a = int(input())






cnt = 0
for i in range(10,a + 1):
    b = list(str(i))

    v1 = 0
    b_len = len(b)
    v2 = int(b[1]) - int(b[0])
    for j in range(1,b_len):
        if int(b[j]) - int(b[j-1]) == v2:
            v1 += 1

    if v1 == b_len-1:

        cnt += 1

if a <= 10:
    print(a)
else:
    print(cnt+9)




