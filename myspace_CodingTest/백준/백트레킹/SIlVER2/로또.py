from itertools import permutations

while True:

    l1 = list(map(int,input().split()))
    if l1 == [0]:
        break
    else:
        l2 = l1[1:len(l1)]
        per = list(permutations(l2,6))
        for lst in per:
            if list(lst) == sorted(lst):
                print(*lst)
    print()



































































