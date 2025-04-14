def solution1(s):
    s2 = ""
    s1 = s
    arr = s1.split(" ")
    arr1 = [int(i) for i in arr]

    if len(set(arr1)) == 1:
        s2 += str(arr1[0])
        s2 += " "
        s2 += str(arr1[0])
    else:
        s2 += str(min(arr1))
        s2 += " "
        s2 += str(max(arr1))

    return s2

# chat gpt4o
def solution(s):
    nums = list(map(int, s.split()))
    return f"{min(nums)} {max(nums)}"

