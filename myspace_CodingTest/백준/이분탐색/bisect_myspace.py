import bisect

arr = [1,3,5,2,4,6,13,10]
arr.sort()
x = 4
print(arr)
left = bisect.bisect_left(arr,x)
print(left)
right = bisect.bisect_right(arr,x)
print(right)