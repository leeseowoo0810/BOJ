a,b,v=map(int,input().split())
cnt = sex = 0
while True:
    if v-a>=0:
        sex+=v-a+b
        cnt+=1
    elif sex<=0:
        print(cnt)
        break
    else:
        print()
    