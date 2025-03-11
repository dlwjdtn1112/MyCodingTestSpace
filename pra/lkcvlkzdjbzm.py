def f(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    return cnt

a,b = map(int,input().split())

print(f(a)//(f(b)*f(a-b)))







