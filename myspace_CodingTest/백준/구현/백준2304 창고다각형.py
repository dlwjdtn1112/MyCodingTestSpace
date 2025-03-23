
N = int(input())
mx_i = 0
mx_result = 0
result_List = [0]*1000
for i in range(N):
    L,H = map(int,input().split())
    result_List[L] = H
    if mx_result < H:
        mx_i,mx_result = L,H



ans = mx = 0

for i in range(0,mx_i+1):
    mx =  max(mx,result_List[i])
    ans += mx
mx = 0
for i in range(999,mx_i,-1):
    mx = max(mx,result_List[i])
    ans += mx

print(ans)



