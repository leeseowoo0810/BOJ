c = s = 100
n=int(input())
for _  in range(n):
    a,b=map(int,input().split())
    if a<b:
        c-=b
    elif a>b:
        s-=a
print(c)
print(s)

