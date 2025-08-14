

T = int(input())

result = []

for _ in range(T):
    string_list = ['S', 'D', 'H', 'C']
    string13 = [13] * 4

    dict_result = dict(zip(string_list, string13))
    s1 = input()
    arr = []
    arr1 = []
    for i in range(0,len(s1),3):
        arr.append(s1[i:i+3])
    if len(arr) != len(set(arr)):
        arr1.append('ERROR')

    else:
        for j in arr:
            dict_result[j[0]] -=1
        for k in dict_result.values():
            arr1.append(k)



    result.append(arr1)


for lst in range(len(result)):
    print(f"#{lst + 1}", end=" ")
    for lst1 in result[lst]:

        print(lst1, end = " ")
    print()



