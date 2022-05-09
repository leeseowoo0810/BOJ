a,b,c=map(int,input().split())
total = 0
if a == b == c:
    total = 10000 + (a * 1000)
elif a != b and b != c and a != c:
    total = max(a,b,c) * 100
else:
    if a == b:
        total = 1000 + (a * 100)
    elif b == c:
        total = 1000 + (b * 100)
    elif a == c:
        total = 1000 + (c * 100)

print(total)