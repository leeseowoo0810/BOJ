N = int(input())
d = 2 

while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)