ysum = ksum=0
for _ in range(int(input())):
    for _ in range(9):
        y,k=map(int,input().split())
        ysum+=y
        ksum+=k

    if ysum>ksum:
        print('Yonsei')
    elif ysum<ksum:
        print('Korea')
    else:
        print('Draw')