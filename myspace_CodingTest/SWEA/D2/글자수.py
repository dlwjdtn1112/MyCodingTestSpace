

result = []

# s1 = list("ZYJZXZTIBSDG")
# s2 = list("TTXGZYJZXZTIBSDGWQLW")
#
# a = len(s1)
# l1 = [0]*a
# d1 = dict(zip(s1,l1))
#
# for i in s2:
#     if i in s1:
#         d1[i] += 1
#     else:
#         pass
#
# print(max(d1.values()))

T = int(input())
for _ in range(T):
    s1 = list(input())
    s2 = list(input())
    a = len(s1)
    l1 = [0] * a
    d1 = dict(zip(s1,l1))
    for i in s2:
        if i in s1:
            d1[i] += 1
        else:
            pass
    result.append(max(d1.values()))

for lst in range(len(result)):
    print("#"+str(lst+1), result[lst])

