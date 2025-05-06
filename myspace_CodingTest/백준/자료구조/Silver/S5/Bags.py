#내가 작성한 코드
N = int(input())

arr = list(map(int,input().split()[:N]))
print(len(set(arr)))