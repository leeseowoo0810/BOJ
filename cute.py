c=0
nc=0
for _ in range (1, int(input())+1):
    a=int(input())
    if a==1:
        c+=1
    elif a==0:
        nc+=1
if c<nc:
    print('Junhee is not cute!')
elif c>nc:
    print('Junhee is cute!')
