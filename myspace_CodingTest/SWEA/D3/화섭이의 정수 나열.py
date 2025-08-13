result = []

T = int(input().strip())

for _ in range(T):
    cnt = 0
    a = int(input().strip())

    s_list = []
    while len(s_list) < a:
        s_list.extend(input().split()) #입력을 여러줄 받을 경우에 extend함수를 작성을 해야 한다.

    s2 = "".join(s_list)


    while True:
        if s2.find(str(cnt)) != -1:
            cnt += 1
        else:
            result.append(cnt)
            break

for lst in range(len(result)):
    print("#" + str(lst + 1), result[lst])
